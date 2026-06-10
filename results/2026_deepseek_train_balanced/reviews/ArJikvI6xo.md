## Summary

This paper proposes GFLAgent, a federated learning system that integrates an LLM-based agent (equipped with memory, computational tools, and Chain-of-Thought reasoning) to dynamically select clients and allocate them to tiers for asynchronous training, alongside a buffer mechanism for handling outlier clients. The idea of applying LLM agents to FL client selection is novel, but the paper as presented has severe specification gaps, a confounded evaluation design, and unsupported claims that collectively prevent acceptance at a top venue.

## Strengths

- **Novel application of LLM-based agents to FL client selection and tier allocation.** The paper proposes a genuinely new idea — using an LLM agent with structured memory (short-term/long-term), dedicated computational tools (text transformation, key information extraction, ML scripts), and CoT reasoning to replace hand-tuned client selection heuristics in tiered FL (Section 4.3.2). Prior tiered-FL work (TiFL, FedAT) relies on rule-based or manually engineered scheduling, which the paper correctly identifies as a limitation.

- **Buffer mechanism for outlier clients addresses a real gap in prior tiered FL systems.** Section 4.2 and Algorithm 1 introduce a buffer zone and monitor that detects and relocates anomalous clients (e.g., disconnected or slowed devices) into a separate update strategy. Earlier tiered frameworks (TiFL, FedAT) lack this capability, as the paper notes (lines 18–20, 100–101).

- **Real hardware measurements on an 8× RTX 3090 setup.** The paper reports efficiency improvements of 37.6% over FedAvg and 8.9% over FedAT (3 Tiers) in terms of training speed, along with energy measurements (Section 5.4). These are hardware-backed results rather than simulation-only claims.

- **Ablation study isolating buffer, agent architecture, and contribution-calculation modules** (Section 5.5, Table 3). This provides an empirical decomposition of design choices, even though the ablation has a critical gap described below.

## Weaknesses

### Major

- **The LLM agent is critically underspecified — the paper's core contribution cannot be reproduced or properly evaluated.** The paper never identifies which LLM drives GFLAgent (GPT-3 appears only in the related work section, line 52). No prompt templates are shown (Section 4.3.1 merely says "by tweaking the prompt templates and key elements, one can effectively manage task scheduling"). The tools are described as "text transformation utilities, key information extraction, data processing capabilities, and foundational machine learning model scripts" — a list of categories, not a specification. The CoT implementation is described as "essentially follows a prompt template to completion" without reproducing the template. The memory mechanism is described at a conceptual level only (Section 4.3.2). Since the LLM agent is the paper's central contribution, this level of underspecification means a reader cannot determine whether the Agent is making genuine decisions or merely acting as an opaque wrapper around simpler heuristics, nor can the work be independently verified or built upon.

- **The "green computing" framing is undermined by incomplete energy accounting.** The paper repeatedly claims GFLAgent is "energy friendly" and meets "green computing" requirements (abstract, line 4, line 20). However, the core innovation runs a Large Language Model (on an 8× RTX 3090 server, Section 5.1.1) as a scheduler making decisions every cycle. The paper measures client-side training energy savings (21.4% less than FedAvg, line 239) but never accounts for the LLM's own inference energy. Line 80 dismisses server energy as "relatively minor" without measurement or justification. If the LLM's energy footprint cancels out or exceeds the client-training savings, the "green" claim collapses. The paper needed at minimum to measure or bound the LLM's energy cost.

- **The experimental comparison confounds the effect of more training rounds with better client selection.** Section 5.2 (line 198) states: "our experiments utilized a time-constraint mode, given that we strategically selected a subset of clients for training; had we adopted the same number of global rounds for training, our model's performance would likely be inferior." This is an honest admission but a critical methodological issue. GFLAgent uses fewer clients per round, completes *more rounds* in the same wall-clock time, and is reported as 5.7× faster in rounds-per-second. Its accuracy advantage could therefore stem entirely from completing more gradient update steps, not from superior client selection. The paper provides no analysis to disentangle these factors — e.g., by holding wall-clock time constant and reporting accuracy curves, or by holding communication rounds constant and showing that GFLAgent's selection strategy still yields better accuracy.

- **The ablation study does not test whether the LLM itself provides any benefit over rule-based methods.** The ablation (Section 5.5, Table 3) compares the full GFLAgent against a "w/o Agent" variant that "represents that there is only one large language model and prompt word template as a simple scheduler." Both conditions use an LLM. This tests whether the Agent architecture (memory, tools, CoT) adds value over a simpler LLM-based scheduler, but it does **not** test the more fundamental question: does using *any* LLM at all outperform a purely rule-based scheduler that doesn't involve an LLM? Without a no-LLM baseline (e.g., random selection, proportional selection based on historical accuracy, or balancing data distributions), the paper cannot claim that LLM-based scheduling drives the improvements.

- **Unsupported claims about abnormal state handling.** Section 5.3.3 (line 232) states "GFLAgent's ability to handle occasional delay situations is quantitatively one order of magnitude higher" — the sentence cuts off with no comparison numbers, no supporting data, and no experimental evidence. This is a strong quantitative claim presented without any supporting evidence.

### Minor

- **Algorithm 1 pseudocode has a likely logic inconsistency.** The first loop (lines 126–128) iterates `r = \hat{R},...,R` running FedAvg. The second loop (lines 129–141) also iterates `r = \hat{R},...,R` running the Agent. If `\hat{R}` is the round at which the Agent is introduced, the warmup should run from 1 to `\hat{R}` (or `\hat{R}-1`), not from `\hat{R}` to `R`. As written, the FedAvg loop and Agent loop cover the same range, which would either double-execute or never execute the intended warmup phase. (This may be a formatting artifact from PDF extraction, but as presented it is confusing.)

- **Energy comparison shows GFLAgent uses *more* energy than a baseline, contradicting the "green" framing.** Line 239 reports that GFLAgent's "training energy consumption is 21.4% lower than FedAvg, and 10.2% higher than its other best model FedBalancer-S." The 10.2% increase over FedBalancer-S is framed positively ("lower than FedAvg, and 10.2% higher than its other best model") but it is directionally worse. The paper does not discuss why this happens or how it squares with the green computing narrative.

- **How outlier clients are detected is never specified.** Section 4.2 and Algorithm 1 (line 134) say "Monitor move abnormal client i to Buffer" but never define what constitutes "abnormal" — no threshold, detection criterion, or anomaly detection method is provided.

- **No statistical significance reporting.** No standard deviations, confidence intervals, or number of independent trials are reported for any experimental result. The reader cannot assess whether reported improvements are statistically significant.

- **Only MNIST is explicitly named as a dataset** (line 191). The paper mentions "standard datasets" (contribution list, line 22) and "all datasets" (Table 2 caption, line 216) but does not name other datasets in the body. If CIFAR-10, Fashion-MNIST, or others were used, they should be stated clearly.

- **Limited evaluation scale: only 20 clients.** FL heterogeneity challenges are often more pronounced at larger scales (100+ clients). This limits the generality of the findings.

- **Section reference errors.** Line 246 references sections "3.4.1" and "3.4.2" which do not exist in the paper's section numbering (the relevant sections are 4.2 and 4.3).

### Trivial

- Equation (5) (line 119) uses the unclear subscript notation `_{\{tier_k,i\in||s||\}}` that is difficult to parse.
- Section 5.3.3 (line 232) contains an incomplete sentence.

## Nice-to-Haves

- Reporting accuracy as a function of both wall-clock time and number of rounds would strengthen the evaluation.
- A larger-scale evaluation (100+ clients) would increase confidence in generalizability.
- Specifying the outlier detection criterion (statistical threshold, performance deviation, etc.) would improve reproducibility.

## Removed Points

*These points are flagged to be removed; treat them with caution:*

- The Strength Finder claimed Section 5.3.3 provides "a concrete robustness advantage" with "one order of magnitude" improvement. This is removed because the paper's own sentence is incomplete and provides no supporting data for this claim — it is an assertion, not evidence.
- The Strength Finder's "first to my knowledge" framing is speculative and removed.
- The Strength Finder's claim that the ablation "systematically" isolates all components is overstated; the ablation is missing the critical no-LLM baseline.
- The Harsh Critic's characterization of the time-constraint issue as making results "difficult to interpret" is accurate, but the critic's suggestion that no proper comparison was done is softened here since the paper acknowledges the limitation honestly — the weakness is the lack of follow-up analysis to disentangle the effects, not the use of time-constraint evaluation per se.
- The Harsh Critic's point about the LLM agent being "the central claim" and "cannot be independently verified" is kept (in Major), but the "structural flaw" label is softened: the issue is severe underspecification, not an inherent flaw in the approach. The criticism is factually correct.

## Novel Insights

The most interesting observation from reviewing this paper is that the LLM underspecification problem and the time-constraint confound interact in a way that makes it impossible to determine whether the LLM agent is doing anything useful at all. Even if the paper had specified the LLM and prompts, the evaluation design conflates training speed (more rounds from fewer clients) with selection quality (choosing the right clients). An ablation that removes the LLM entirely and uses a simple heuristic (e.g., random selection) would simultaneously address both issues: it would test whether the LLM adds value and, if the heuristic matched GFLAgent's performance, would demonstrate that the time-constraint advantage (faster rounds) accounts for the gains. The paper's current ablation only compares two LLM-based variants, so this question goes unanswered.

## Suggestions

1. **Specify the LLM model, prompts, and decision protocol.** The paper cannot function as a scientific contribution without stating which LLM is used, providing the prompt templates (or examples), and describing how LLM outputs are parsed into scheduling decisions.

2. **Add a no-LLM baseline to the ablation.** Compare the full GFLAgent against an otherwise identical system where client selection and tier allocation are done by a simple rule (e.g., random selection, proportional selection, or balancing data distributions). This is the most direct test of whether the LLM provides value.

3. **Disentangle round count from selection quality.** Report accuracy as a function of both wall-clock time and number of communication rounds. Include an analysis that holds either dimension constant to isolate the effect of better client selection.

4. **Account for the LLM's own energy consumption.** Measure or bound the energy cost of LLM inference and show that the net effect (client savings minus LLM overhead) is positive, or drop the "green computing" framing.

5. **Support or remove the "one order of magnitude" claim.** Either provide the experimental data backing this claim or remove it.

6. **Define the outlier detection criterion.** Specify what threshold or method is used to identify "abnormal" clients.

7. **Report statistical variation** (standard deviations over multiple runs with different seeds).

## Score and Decision

**Overall assessment:** The paper proposes a genuinely novel idea — applying LLM agents to client selection in heterogeneous federated learning — and the buffer mechanism is a reasonable design addition. However, the paper has critical deficiencies for a top venue: the LLM agent (the core contribution) is specified at such a high level that the work cannot be reproduced or properly evaluated; the experimental design conflates the effect of more training rounds with better client selection; the "green computing" claim ignores the LLM's own energy footprint; the ablation does not test whether the LLM provides any benefit; and multiple claims are made without supporting evidence. These issues collectively prevent acceptance in current form.

MY FINAL SCORE: <score>3.5</score>
MY FINAL DECISION: <decision>Reject</decision>