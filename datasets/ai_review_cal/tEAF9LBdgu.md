- Decision: Reject
- Avg Score: 6.75
- Scores: 8, 8, 5, 6
Now I have a thorough understanding of the paper and the reviewer claims. Let me produce the consolidated review.

## Summary

AutoGen is an open-source framework for building LLM applications via multi-agent conversations. It introduces two core abstractions: **conversable agents** (agents that can flexibly combine LLMs, humans, and tools) and **conversation programming** (a paradigm that unifies complex workflows as multi-agent interactions). The paper demonstrates six diverse applications (math reasoning, retrieval-augmented QA, embodied decision-making, supply-chain coding, group chat, chess) and reports benchmark results in figures.

---

## Strengths

- **Customizable conversable agents that integrate LLMs, humans, and tools (Section 2.1):** The paper defines a clean abstraction where an agent can be backed by LLM inference, human input, tool execution, or any combination. The built-in `AssistantAgent` and `UserProxyAgent` are concrete, reusable implementations of this design — a practical contribution that has seen real-world adoption.

- **Conversation programming as a unifying paradigm (Section 2):** The framework centers development around two steps — defining agents and programming their interaction behavior — using a mix of natural language and code. This abstraction demonstrably covers a wide range of conversation patterns across the six applications, from static two-agent loops to dynamic group-chat speaker selection (A5) and turn-taking with legality constraints (A6).

- **Breadth of demonstrated applications (Section 3, Figure 2):** The six applications span mathematics, coding, QA, operations research, online decision-making, and entertainment. This breadth provides evidence that the framework generalizes beyond a single task domain.

- **Configurable human-in-the-loop (Section 2.1):** The `UserProxyAgent` allows developers to specify when and how often human input is solicited, including the option to skip entirely. This enables a smooth spectrum from full automation to human agency, a practical design choice for real-world deployment.

---

## Weaknesses

### Major

- **Core claims about reduced development effort are asserted without visible evidence.** The paper claims that AutoGen enables "reduced development code" and "decreased manual burden" (abstract, line 59; Discussion, line 147). However, no quantitative evidence is presented in the visible text to support this — no lines-of-code comparisons, no development time measurements, no user study, and no structured comparison against alternative frameworks. For a paper whose value proposition includes development efficiency, this is a significant gap. The claim is stated as a finding rather than demonstrated.

- **The paper does not critically discuss limitations or failure modes.** Multi-agent conversations incur higher cost (multiple LLM calls per task) and higher latency, and introduce new failure modes such as agents collectively converging on wrong answers, conversation loops that never terminate, and brittle reliance on prompt engineering. The Discussion (Section 4) acknowledges only "new safety challenges" and the need to "optimize[e] overall efficiency" in generic terms, but never concretely examines when the framework *does not* help or what failure patterns practitioners should expect. For a systems paper proposing a general-purpose framework, this omission weakens the contribution's practical credibility.

- **The conceptual novelty of "conversable agents" is high-level and the visible description does not sharply distinguish from prior agent frameworks.** Section 2.1 describes agents as entities that can pass messages and be backed by LLMs, humans, or tools. This abstraction overlaps substantially with existing frameworks (LangChain, Semantic Kernel, etc.). The paper does not articulate what specific mechanism or design insight makes AutoGen's agent abstraction *different* beyond being "conversable." The "conversation programming" section (Section 2.2) where the novel control mechanisms likely reside was stripped by the parser, so its technical depth cannot be evaluated from the visible text.

### Minor

- **No quantitative results are reported in the visible main-text prose.** The empirical results are presented only in figures (Figure 4a–d). The captions provide qualitative summaries ("most competitive performance," "improve performance") but no exact numbers, effect sizes, or variance estimates. While figures are standard, reporting key numbers in prose (e.g., "AutoGen achieves X% on MATH vs. Y% for single-agent baseline") would make the evaluation immediately assessable. (Note: detailed results may appear in the stripped application sections.)

- **The two "critical questions" posed in the Introduction (lines 28–29) are not explicitly revisited with a structured mapping to design solutions.** The paper asserts that conversable agents answer question 1 and conversation programming answers question 2, but the Introduction does not trace this mapping clearly. The connection is asserted rather than argued, making the conceptual framing less crisp than it could be.

### Trivial

- None beyond those already noted as minor.

---

## Nice-to-Haves

- An ablation study isolating the contribution of the multi-agent conversation design (e.g., single-agent vs. two-agent vs. three-agent on the same task) would strengthen the claim that the framework architecture — not just the underlying LLM — drives performance.
- A cost and latency comparison between AutoGen and single-agent baselines would help practitioners understand when the multi-agent overhead is justified.
- Including a brief structured comparison with related frameworks (LangChain, CrewAI, MetaGPT) in the main text would help readers situate the contribution, though this is not a fatal omission.

---

## Removed Points

*These points were raised by reviewers but are excluded from the main weaknesses for the reasons below:*

- **"Empirical evidence is inaccessible" (harsh critic #1):** The paper includes Figure 4 with results in subfigures. The detailed application sections (A1–A6) were stripped by the PDF text extractor; they existed in the original submission. Criticisms that depend on content the parser removed are not chargeable to the authors.
- **"No baseline comparisons" (harsh critic):** Baseline comparisons were in the stripped application sections (A1–A6). Parser artifact, not author omission.
- **"Missing related works" (harsh critic):** Per the review guidelines, I cannot confirm which related works are or are not cited without external sources.
- **"Missing ablation studies" / "reproducibility details absent" (harsh critic):** These were in sections stripped by the parser (application details, experimental setup).
- **The harsh critic's claim that the paper does not distinguish from LangChain etc.:** While the novelty question is valid (kept as a minor weakness above), the critic's stronger framing — that the method "description is too abstract" — partly depends on the stripped conversation programming section which presumably contained the detailed mechanism. Weakened version retained as minor.
- **Strength Finder's claims about specific numerical benchmark results outperforming SOTA:** The figure captions only provide qualitative directional claims ("most competitive," "improve performance"). Exact numerical comparisons cannot be confirmed from visible text, so these strength claims are tempered. The breadth and diversity of applications remain verifiable strengths.

---

## Novel Insights

None beyond the paper's own contributions. The two reviewers offer standard observations that align with the paper's stated framing — neither identifies a weakness or strength that the paper itself does not acknowledge or could not address with straightforward revisions.

---

## Suggestions

1. **Add a main-text table** with key numerical results (AutoGen vs. strongest baseline per task) so the empirical contribution is immediately evaluable without consulting figures.
2. **Add a limitations subsection** to the Discussion that concretely enumerates known failure modes, cost/latency trade-offs, and patterns where the multi-agent approach underperforms a simpler alternative.
3. **Replace the qualitative "reduced development code" claim** with at least a rough quantitative comparison (e.g., lines of code for equivalent functionality vs. a non-framework implementation) or, failing that, reframe the claim as qualitative flexibility rather than quantitative reduction.
4. **Strengthen the conceptual framing** by explicitly returning to the two critical questions from the Introduction in the Framework section and mapping each design decision to the question it addresses.

---
