A few months ago, an acquaintance of mine made a post on Twitter (X) about what constitutes a good code review, looking from both the reviewer’s and the submitter’s perspective. At the time, I had already put together a draft list on this topic (since I was a Tech Lead at a company for a period, and one of the needs was to have a well-defined, objective, and, as much as possible, deterministic process).

However, this original list was more of a guide for reviewers than for submitters. That said, the second group plays a significant role in the success or failure of the review process. So, I found it interesting to expand this list to include the submitter's role, and as a result, I shared it on Twitter (X).

But given the recent issues and disagreements affecting Twitter (X) (especially in Brazil), I decided to bring this checklist (I didn't want to call it a checklist, but that’s fine, it can be considered one) to my blog and write this post you're reading now.

Enough with the preamble, let's get to the main points. Below is the list of items for each of the roles. I thought it would be wise to include a section called "General," which is common to both roles, but feel free to change or add items as needed for your team or the process your company follows (I made a few adjustments from the original to make this list a bit more generic).

### General:

- Design Patterns: Check what is implemented in the project, but don't be strictly tied to them. They might be poor choices, and if you find a better solution, make suggestions and / or discuss about it.

### As a Reviewer:

1. Unit tests (run both unit and full suite tests);
   - If the routine has no coverage (i.e., zero tests), a description of the reason is required;
2. Verify if formatting and static code analysis tools (lint) have been applied;
3. Review the code and its structure;
   - Unused imports;
   - Dead code;
   - Variables with inconsistent naming conventions (snake_case, camelCase, PascalCase);
   - Unused variables;
   - Variables with non-meaningful names (even if complying with naming rules);
   - Unhelpful, unclear, or outdated comments;
   - Structure (well-defined functions | classes);
   - Code repetition;
   - Cognitive complexity;
     - Number of lines in the file (preferably between 300-500 lines, avoid files with 1k lines, for example);
     - Too many functionalities in a single file (better organization or splitting needed);
     - Unconventional data structures for the language (provide necessary justification);
     - Excessive use of third-party libraries unnecessarily;
     - Verify if breaking down into smaller functions and organizing them within the file is well-ordered;
     - Very deep nesting (a maximum of 4-5 levels);
     - Large decision structures (e.g., ifs with many `and` or `or`);
     - Recursive functions (should be carefully managed in non-functional languages);
     - Break and continue clauses should be used (excessive use discouraged), but attention should be given to how they affect flow;
   - Language-specific rules (e.g., Python - prefer list comprehensions over map, filter, reduce when possible);
4. Always ensure the code addresses the requested business rule.

### As a Submitter:

1. (All the rules above);
2. PR creation should include:
   - Add useful descriptions, comments, and documentation to the code;
   - If it's frontend, add videos or images;
   - If it's backend, add API calls and parameters;
   - Add information about necessary environment variables;
   - Dependencies between projects (if your code depends on another project to run);
   - Tags or labels to facilitate searching;
   - If the project doesn't have Owners, add 1-2 Owners for the PR;
   - Merge only after approval from at least 2 reviewers;
   - If the project has CI/CD, verify it passes;
3. After merge:
   - Verify if the deployment was successful;
   - Inform the team/lead about the deployment.

## Refactoring

I think it's worth talking a bit about code refactoring. While it could be included as a topic in a checklist, it's more of an issue beyond that scope (in fact, it could definitely be one of the aspects to evaluate). But I believe this subject deserves its own section (I won’t dive too deep into it here, of course).

Recently, I read Kent Beck's book [_Tidy First_](https://www.amazon.com.br/Tidy-First-Personal-Exercise-Empirical/dp/1098151240), and although it's short (about 100 pages), it brought me an interesting reflection on code refactoring, which, in a way, aligned with what I've always thought: perform small refactorings when possible and avoid large-scale ones.

![Tidy First](/static/pages/essays/18/image.jpg)

One of the points Kent emphasizes in the book is that small refactorings are easier to observe and review, thus making their approval smoother.

Therefore, I believe this is an extremely useful tip: if you notice code that needs refactoring in your PR, go ahead and refactor it, but make sure it’s small, atomic, and doesn’t affect the functionality of the code.

## Update

After making this post, my acquaintance shared some cool information that his team provided.
A Code Review pyramid. I found it really interesting and decided to include it here as an update to this post, along with the link to the original post that brought this pyramid as a reference.

One important thing, which is exactly one of the points highlighted in the Code Review Pyramid, is that many checks can be automated. This is an important aspect to consider because anything that can be automated is, in a sense, more objective and practical.

[The Code Review Pyramid](https://www.morling.dev/blog/the-code-review-pyramid/)

![The Code Review Pyramid](/static/pages/essays/18/image2.jpg)

## References

- [Sonar on Cyclomatic Complexity](https://www.sonarsource.com/learn/cyclomatic-complexity/)
- [Sonar on Cognitive Complexity](https://www.sonarsource.com/resources/cognitive-complexity/)
- [5 Clean Code Tips for Reducing Cognitive Complexity](https://www.sonarsource.com/blog/5-clean-code-tips-for-reducing-cognitive-complexity/#tip-3-nesting-things-can-make-things-bad-really-fast)
- [The Code Review Pyramid](https://www.morling.dev/blog/the-code-review-pyramid/)
