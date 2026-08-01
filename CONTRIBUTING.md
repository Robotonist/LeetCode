# Contributing to LeetCode Solutions

Thank you for your interest in contributing! This document provides guidelines for contributing to this repository.

## How to Contribute

### 1. Adding a New Solution

- Create a file in the appropriate difficulty folder (`Easy/`, `Medium/`, or `Hard/`)
- Follow the file naming convention: `{NUMBER:03d}-{PROBLEM_NAME}.{EXTENSION}`
- Use the solution template (see README.md)
- Include:
  - Problem description and link
  - Clear explanation of your approach
  - Time and space complexity analysis
  - Comments for complex logic
  - Edge case handling
- Update `Solutions.md` with your new entry
- Update statistics in README.md

### 2. Improving Existing Solutions

- Optimize for better time/space complexity
- Add solutions in new languages
- Improve documentation and comments
- Fix bugs or edge cases
- Enhance problem explanations

### 3. Code Style Guidelines

**Python:**
- Follow PEP 8 style guide
- Use meaningful variable names
- Add type hints where appropriate
- Include docstrings

**Java/C++:**
- Follow standard conventions for the language
- Use clear, descriptive variable names
- Include comments for complex sections

### 4. Commit Messages

Use clear, descriptive commit messages:

```
Add solution for Problem 001: Two Sum
Optimize solution for Problem 015: 3Sum
Fix edge case in Problem 042: Trapping Rain Water
```

### 5. Pull Request Process

1. Fork the repository
2. Create a feature branch: `git checkout -b add/problem-XXX`
3. Make your changes
4. Commit with clear messages
5. Push to your branch
6. Create a Pull Request with a description

### 6. PR Description Template

```markdown
## Changes
Briefly describe what was added or changed.

## Problem(s) Affected
- Problem XXX: [Name]

## Type of Change
- [ ] New solution
- [ ] Optimization
- [ ] Bug fix
- [ ] Documentation

## Checklist
- [ ] Code follows style guidelines
- [ ] Comments/documentation added
- [ ] Solutions.md updated
- [ ] No breaking changes
```

## Questions or Issues?

Feel free to:
- Open an issue for bugs or suggestions
- Use GitHub Discussions for questions
- Check existing issues/PRs before creating duplicates

## Code of Conduct

- Be respectful and constructive
- Help others learn and improve
- Focus on the quality of solutions
- Respect different approaches and languages

Thank you for contributing! 🎉
