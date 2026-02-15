# GitHub Actions Quick Reference Guide

## 🎯 Workflow Features at a Glance

### Operating Systems Coverage
```
┌─────────────────────────────────────────┐
│  OPERATING SYSTEMS (all x86_64)         │
├─────────────────────────────────────────┤
│  ✓ Linux   (ubuntu-latest)              │
│  ✓ Windows (windows-latest)             │
│  ✓ macOS   (macos-13)                   │
└─────────────────────────────────────────┘
```

### Branch Restrictions
```
┌─────────────────────────────────────────┐
│  BRANCHES THAT TRIGGER WORKFLOW         │
├─────────────────────────────────────────┤
│  ✓ main                                 │
│  ✓ develop                              │
│  ✓ feature/*  (all feature branches)    │
│  ✗ Others (hotfix, bugfix, etc.)        │
└─────────────────────────────────────────┘
```

### Concurrency Control
```
┌─────────────────────────────────────────┐
│  CONCURRENCY LIMITS                     │
├─────────────────────────────────────────┤
│  Workflow Level:  1 per branch          │
│  Job Level:       2 parallel max        │
│  Cancel Old:      Yes (in-progress)     │
└─────────────────────────────────────────┘
```

## 📊 Job Dependency Graph

```
                    START
                      │
                      ▼
        ┌─────────────────────────────┐
        │  pre-build-validation       │
        │  - Checks changes            │
        │  - Sets version              │
        │  - Validates structure       │
        └──────────────┬──────────────┘
                       │
         ┌─────────────┼─────────────┐
         │             │             │
         ▼             ▼             ▼
   ┌─────────┐  ┌─────────┐  ┌─────────┐
   │ Linux   │  │ Windows │  │ macOS   │
   │ Build   │  │ Build   │  │ Build   │
   │         │  │         │  │         │
   │ Matrix: │  │ Single  │  │ Single  │
   │ 2 jobs  │  │ x86_64  │  │ x86_64  │
   └────┬────┘  └────┬────┘  └────┬────┘
        │            │            │
        └────────────┼────────────┘
                     │
        ┌────────────┴────────────┐
        │                         │
        ▼                         ▼
   ┌──────────┐            ┌───────────┐
   │Integration│            │Deployment │
   │  Tests    │            │   Prep    │
   │           │            │(main only)│
   └─────┬────┘            └─────┬─────┘
         │                       │
         └───────────┬───────────┘
                     │
                     ▼
            ┌────────────────┐
            │ Workflow       │
            │ Summary        │
            │ (always runs)  │
            └────────────────┘
                     │
                     ▼
                    END
```

## 🔄 Execution Patterns

### Serial Execution
```
Job A ──> Job B ──> Job C
```
Example: `pre-build-validation → build-linux → integration-tests`

### Parallel Execution
```
        ┌──> Job B
Job A ──┤
        └──> Job C
```
Example: `builds → [integration-tests || deployment-prep]`

### Matrix Execution with Limits
```
Job (Matrix) ──> [ Config 1 ]  ◄─┐
                 [ Config 2 ]    │ Max 2
                 [ Config 3 ]  ◄─┘ at once
```
Example: Linux builds with gcc and clang

## 🎛️ Key Configuration Sections

### 1. Workflow Triggers
```yaml
on:
  push:
    branches: [main, develop, feature/**]
  pull_request:
    branches: [main, develop]
  workflow_dispatch:
```

### 2. Concurrency
```yaml
concurrency:
  group: ${{ github.workflow }}-${{ github.ref }}
  cancel-in-progress: true
```

### 3. Job with Dependencies
```yaml
job-name:
  needs: [dependency1, dependency2]
  if: needs.dependency1.outputs.value == 'true'
  runs-on: ubuntu-latest
```

### 4. Matrix Strategy
```yaml
strategy:
  fail-fast: true
  max-parallel: 2
  matrix:
    config:
      - { arch: "x86_64", compiler: "gcc-11" }
      - { arch: "x86_64", compiler: "clang-14" }
```

### 5. Artifact Management
```yaml
# Upload
- uses: actions/upload-artifact@v4
  with:
    name: my-artifact
    path: build/
    retention-days: 7

# Download
- uses: actions/download-artifact@v4
  with:
    name: my-artifact
    path: artifacts/
```

## 🛠️ Common Commands by OS

### Linux (Bash)
```yaml
- name: Example Step
  run: |
    echo "Architecture: $(uname -m)"
    mkdir -p build
    ls -la
```

### Windows (PowerShell)
```yaml
- name: Example Step
  shell: powershell
  run: |
    Write-Host "Architecture: $env:PROCESSOR_ARCHITECTURE"
    New-Item -ItemType Directory -Path build
    Get-ChildItem
```

### macOS (Bash)
```yaml
- name: Example Step
  run: |
    echo "Architecture: $(uname -m)"
    sw_vers -productVersion
    brew --version
```

## 🔍 Architecture Verification

### Linux
```bash
ARCH=$(uname -m)
# Expected: x86_64
```

### Windows
```powershell
$arch = $env:PROCESSOR_ARCHITECTURE
# Expected: AMD64
```

### macOS
```bash
ARCH=$(uname -m)
# Expected: x86_64
```

## 📝 Context Variables

| Variable | Description | Example Value |
|----------|-------------|---------------|
| `github.ref` | Full ref | `refs/heads/main` |
| `github.ref_name` | Branch name | `main` |
| `github.sha` | Commit SHA | `abc123...` |
| `github.actor` | User who triggered | `username` |
| `github.event_name` | Event type | `push` |
| `github.workflow` | Workflow name | `CI/CD Demo` |
| `runner.os` | OS name | `Linux` |
| `runner.arch` | Architecture | `X64` |
| `job.status` | Job status | `success` |

## 🎨 Conditional Expressions

### Common Conditions
```yaml
# Check branch
if: github.ref == 'refs/heads/main'

# Check event type
if: github.event_name == 'pull_request'

# Check job result
if: needs.build.result == 'success'

# Always run
if: always()

# Run on success
if: success()

# Run on failure
if: failure()

# Multiple conditions
if: success() && github.ref == 'refs/heads/main'

# String matching
if: startsWith(github.ref, 'refs/heads/feature/')
```

## ⚙️ Job Outputs

### Setting Outputs
```yaml
steps:
  - name: Set Output
    id: my-step
    run: |
      echo "my-value=hello" >> $GITHUB_OUTPUT
```

### Using Outputs
```yaml
# In same job
${{ steps.my-step.outputs.my-value }}

# In dependent job
needs: job-name
run: echo "${{ needs.job-name.outputs.my-value }}"
```

## 🔄 Workflow Status Summary

| Symbol | Meaning |
|--------|---------|
| ✅ | Job succeeded |
| ❌ | Job failed |
| ⏭️ | Job skipped |
| 🔄 | Job running |
| ⏸️ | Job queued |
| ⚠️ | Job completed with warnings |

## 📊 Timing Expectations

```
Pre-Build Validation:     ~30 seconds
Each OS Build:           ~1-2 minutes
Integration Tests:        ~1 minute
Deployment Prep:          ~30 seconds
Summary:                  ~10 seconds
────────────────────────────────────
Total (serial):          ~8-10 minutes
Total (with parallel):   ~4-6 minutes
```

## 🚀 Performance Tips

1. **Use caching** for dependencies
   ```yaml
   - uses: actions/cache@v3
     with:
       path: ~/.npm
       key: ${{ runner.os }}-node-${{ hashFiles('**/package-lock.json') }}
   ```

2. **Limit artifact size**
   ```yaml
   retention-days: 7  # Don't keep forever
   ```

3. **Use fail-fast** to stop on first failure
   ```yaml
   strategy:
     fail-fast: true
   ```

4. **Parallel jobs** where possible
   ```yaml
   needs: [job1, job2]  # Both run in parallel
   ```

5. **Conditional execution** to skip unnecessary work
   ```yaml
   if: github.event_name == 'push'
   ```

## 📋 Checklist for New Workflows

- [ ] Define clear job dependencies
- [ ] Set appropriate concurrency limits
- [ ] Add branch restrictions if needed
- [ ] Implement architecture verification
- [ ] Use fail-fast for matrix jobs
- [ ] Set artifact retention policies
- [ ] Add descriptive names and comments
- [ ] Include error handling
- [ ] Test manual trigger (workflow_dispatch)
- [ ] Document expected behavior

## 🎯 This Demo Includes

✅ All major OS platforms (Linux, Windows, macOS)  
✅ x86_64 architecture only  
✅ Branch restrictions (main, develop, feature/*)  
✅ Max 2 concurrent jobs  
✅ Serial job dependencies  
✅ Parallel job execution  
✅ Matrix strategies  
✅ Fail-fast behavior  
✅ Conditional execution  
✅ Artifact management  
✅ Comprehensive documentation  

## 🔗 Quick Links

- Main workflow: `comprehensive-demo-workflow.yml`
- Full README: `README.md`
- GitHub Actions Docs: https://docs.github.com/actions

---

**Pro Tip**: Print this page and keep it handy while learning GitHub Actions!
