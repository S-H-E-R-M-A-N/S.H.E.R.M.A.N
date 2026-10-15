Accessibility
We believe that technology should be welcoming, empowering, and usable for everyone, regardless of physical ability, sensory characteristics, cognitive differences, or the tools and devices they use to navigate. Everyone deserves equal access to use, learn from, and contribute to S.H.E.R.M.A.N.

This document outlines our accessibility commitments, the practical standards we strive to uphold, what we expect from our contributors, and how you can report barriers or request assistance if something gets in your way.

Priorities
We prioritize ensuring that core tasks—such as navigating documentation, exploring features, configuring settings, using interactive components, and submitting contributions—can be completed successfully by everyone, regardless of how they interact with our interface.

We use the Web Content Accessibility Guidelines (WCAG) 2.1 Level AA as an aspirational guide for our design and development practices. (Note: This is an ongoing goal and guiding standard for our work rather than a formal third-party certified conformance claim.)

Our primary areas of focus include:

Keyboard Navigation: Ensuring every interactive element is clearly visible, reachable, and fully operable using only a keyboard or switch device.

Screen Reader Compatibility: Providing meaningful structural landmarks, logical heading hierarchies, and appropriate ARIA attributes so content is accurately conveyed through assistive technologies.

Content and Language Support: Using clear, plain language in our documentation and ensuring sufficient color contrast and readable typography across all views.

Contributor expectations
We view accessibility as a shared responsibility across the S.H.E.R.M.A.N community. We expect all user-facing contributions to respect and uphold our accessibility standards.

Testing: Contributors should verify keyboard operability and check color contrast for any new or modified user interface components.

Continuous Integration: Our automated testing pipeline runs accessibility checks on pull requests. Pull requests that introduce automated accessibility regressions will require remediation before merging.

Documentation & Evidence: When submitting user-facing changes, please include a brief note in your pull request description detailing how you tested the feature (e.g., keyboard-only navigation, screen reader checks) and any relevant screenshots or notes.

Reporting accessibility issues
If you encounter an accessibility barrier while using S.H.E.R.M.A.N or reading our documentation, please let us know so we can address it. You can report a barrier by opening an issue on our GitHub repository with the accessibility label, or by contacting our maintainers directly.

To help us understand and resolve the issue quickly, please share as much context as you are comfortable providing:

The task you were trying to complete.

The specific page, component, or URL where the barrier occurred.

What you expected to happen versus what actually happened.

Your browser, operating system, and any assistive technology you were using.

Screenshots and screen recordings are entirely optional. You are never required to disclose personal medical details or disability information to receive support.

Severity
To help our team triage and prioritize fixes effectively, we categorize reported accessibility issues based on how strongly a barrier affects a user's ability to complete a task:

Critical: Prevents a user from completing a core task entirely, and no workaround is available (e.g., a modal dialog that traps keyboard focus with no way to close it).

Major: Significantly impairs the user experience or creates a major obstacle, but a complex workaround exists (e.g., low-contrast text that is difficult to read on certain displays).

Minor: A noticeable cosmetic or minor structural imperfection that does not block core task completion (e.g., an icon missing a decorative alt attribute).

Maintainers will review and assign severity during issue triage. Reporters do not need to determine severity themselves.

How we respond
After you submit an accessibility issue, you can expect the following process:

Acknowledgement: We aim to acknowledge new accessibility reports within 3 business days.

Status Updates & Workarounds: We will provide updates as we investigate the issue, and where possible, offer temporary workarounds for blocked tasks.

Timelines: While resolution timelines vary depending on complexity and maintainer availability, critical barriers are prioritized for upcoming patch releases.

Verification: Once a fix is deployed, we warmly invite reporters to help us verify that the barrier has been successfully removed.

Ownership and maintenance
Accessibility oversight for S.H.E.R.M.A.N is managed by the core maintainer team, with designated accessibility leads responsible for reviewing pull requests, auditing documentation, and handling reported barriers.

Review Cadence: This statement and our core accessibility practices are reviewed annually.

Knowledge Transfer: When team responsibilities shift, accessibility ownership is explicitly handed over during maintainer onboarding to ensure ongoing continuity and accountability.

Supported environments
We actively test and support S.H.E.R.M.A.N across modern desktop and mobile environments:

Browsers: Recent stable versions of Chrome, Firefox, Safari, and Microsoft Edge.

Assistive Technologies: Commonly used screen readers (such as NVDA, VoiceOver, and Orca) and standard keyboard navigation interfaces.

Note: While the project may function in older or unlisted environments, we cannot guarantee full support or optimal assistive technology integration outside of our tested baseline.

Known limitations
We are committed to continuous improvement, but some areas of S.H.E.R.M.A.N currently have known barriers:

Some embedded tutorial videos or complex graphics lack synchronized audio descriptions or full closed captions (tracked in Issue #[Number]). Workaround: Full text transcripts are provided directly beneath each item in the documentation.

Certain advanced data views or interactive data tables lack full column/row header associations for screen readers (tracked in Issue #[Number]). Workaround: Raw data exports are available for download on all data views.

If you encounter a limitation not listed here, please let us know using our reporting process.

Feedback and improvements
We welcome your feedback on how we can make this statement and S.H.E.R.M.A.N more inclusive and welcoming. If you have suggestions for improvement, please open a discussion or pull request on our repository.

If you have encountered an active accessibility barrier, please use the Reporting accessibility issues section above so our team can address it promptly.
