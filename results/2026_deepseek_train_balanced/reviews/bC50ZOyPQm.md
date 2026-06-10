## Summary

READ proposes using a small RNN as a side network attached to a frozen T5 backbone to learn "corrections" to the backbone's hidden states, avoiding backpropagation through the backbone. The paper reports that READ achieves comparable GLUE accuracy to full fine-tuning (84.97% vs 84.52% on T5-BASE) while reducing GPU energy consumption by ~84% and training memory by ~56%, with trainable parameters growing sub-linearly with backbone size.

---

## Strengths

1. **Strong empirical efficiency numbers.** Table 1 shows READ (T5-BASE) achieving 84.97% average GLUE score at 2.06 kWh vs. Full-tuning's 84.52% at 12.52 kWh—an 84% energy reduction—and READ-large (T5-LARGE) achieving the best overall score (85.73%) while consuming less energy than most baselines. These results directly support the paper's central efficiency claim.

2. **Parameter scalability is a genuine architectural advantage.** The paper demonstrates (Table 1 and Figure `adapted_size_backbone_size`) that READ's trainable parameter percentage *decreases* as backbone size increases (0.80% for T5-BASE → 0.32% for T5-LARGE), while Adapter and LoRA grow linearly. The recurrent architecture's decoupling from backbone depth is a concrete, non-obvious contribution.

3. **No pre-training stage for the side network.** Unlike Ladder-Side Tuning (LST), which requires a distillation-based pre-training stage to initialize the side Transformer, READ uses standard RNNs and FFNs with no pre-training (line 81). This is a practical advantage clearly stated and justified.

4. **Inference overhead is substantially lower than the prior side-tuning method.** The paper reports that LST incurs 40% more inference memory and 77% longer inference time than READ (line 196), which is a meaningful practical distinction given LST is the closest prior work.

---

## Weaknesses

### Fatal
None.

### Major

1. **The method is not formally specified.** This is the most serious weakness for a new-method paper at a top venue. The "Breaking Down READ" section (lines 55–99) describes the architecture entirely in prose: "a standard RNN and a Joiner network," "iterative computation of RNN hidden states," "the equation system"—but no equations, no algorithm pseudocode, and no tensor-level description are provided. What exactly is the "equation system" being modeled? What does the Joiner network map from/to? How are RNN hidden states initialized, iterated across layers, and combined with backbone outputs? What are the dimensions of each computation? The paper mentions computing \(x_i\) (line 98) without ever defining \(x_i\). A reader cannot reproduce READ from this description alone. For a conference where method specification is the baseline expectation, this is a major deficit.

2. **Claimed "theoretical justification" does not exist.** Contribution item 4 (line 50) explicitly promises "theoretical justification for utilizing the backbone hidden state for side-tuning." The paper contains no such justification. Definition 1 (lines 88–91) simply defines \(\delta\phi_i = \phi'_i - \phi_i\), which is a definition, not a theoretical argument. The phrase "operates only on the column space of \(\phi\)" (line 99) is dropped without explanation, proof, or consequence. This is not an underdeveloped section—it is a claimed contribution that the paper does not deliver.

3. **Energy measurement methodology is completely unspecified.** The paper's two headline numbers (84% energy reduction, 56% memory reduction) depend entirely on the energy measurements in Table 1. The only description is "We take the cumulative energy consumption and measure the peak GPU during training" (line 129). No information is given about: the measurement tool (nvidia-smi? wall-socket power meter?), time window, whether measurements are GPU-only or system-wide, the GPU hardware model, or whether all methods were run under identical conditions. Without this, the quantitative energy claims are unverifiable.

### Minor

4. **Overstatement of PETL limitations contradicted by own data.** The paper claims that PETL methods "do not reduce the compute cost required to fine-tune" (line 132). However, Table 1 shows Adapter at 6.99 kWh (44% below Full-tuning's 12.52 kWh) and LoRA at 10.58 kWh (15% below). These are non-trivial reductions that contradict the blanket statement. The abstract's claim that PETL methods "marginally reduce memory requirements" is about memory (not directly testable from the table), but the compute-cost claim is testable and inaccurate.

5. **Ablation raises unanswered questions about the role of recurrence.** Table 2 shows that removing recurrence yields a non-recurrent variant achieving 85.15 (vs. READ's 84.97) on T5-BASE and 85.02 (vs. READ-large's 85.73) on T5-LARGE—comparable or slightly better accuracy on BASE, worse on LARGE. The paper frames this as validating recurrence's role in parameter efficiency (0.8% vs. 9.6% params), which is fair. However, the paper does not analyze *why* recurrence is the right inductive bias or whether the accuracy difference on LARGE is significant given the parameter asymmetry. The reader is left wondering whether the RNN component is doing anything qualitatively useful beyond reducing parameters.

6. **No variance or significance statistics.** Results are averaged over 3 seeds (Table 1 caption) with no standard deviations. For methods with close averages (e.g., READ 84.97 vs. Adapter 85.04), this makes it impossible to assess whether differences are meaningful.

7. **RTE excluded from GLUE.** The paper excludes RTE (line 115) due to its small size, which reduces direct comparability with the large body of PETL work reporting 8-task GLUE averages.

### Trivial
None.

---

## Nice-to-Haves

- Compare against original LST published results (not just a re-implementation) to validate the re-implementation's fidelity.
- Include a table of memory savings at multiple backbone scales (the 43% savings at T5-3B is mentioned in a figure caption but not tabulated).
- Provide standard deviations or confidence intervals for key comparisons where scores are close.

---

## Removed Points

These points were flagged by the reviewers but are removed or downgraded for the following reasons:

- *Critic's claim that the commuting diagram is not explained in text*: This is a minor presentation issue that is not a substantive weakness; the diagram itself exists in the paper (Figure 2b) and the concept is described.
- *Critic's concern about LST re-implementation fidelity being "significant"*: Re-implementing baselines is standard practice; the concern is speculative and the paper does describe the pruning method used. Downgraded from the critic's framing.
- *Strength Finder's claim that "Ablation validates the recurrence design choice"*: The ablation does validate the parameter-efficiency benefit of recurrence, but the accuracy parity/close scores mean the framing as "validating" the design choice is too generous. Kept as a qualified observation.
- *Critic's claim that PETL methods "marginally reduce memory" is contradicted by energy data*: The abstract's claim is about *memory*, while the critic uses *energy* data to counter it. These are different quantities. The valid concern (compute cost overstatement) is retained as a minor weakness.

---

## Novel Insights

None beyond the paper's own contributions. The reviews surface the familiar tension between underspecified methodology and strong empirical results but do not produce a synthetic observation that the paper itself does not already contain.

---

## Suggestions

1. **Specify READ completely.** Provide the forward-pass equations: definte the Joiner network's input/output mapping, the RNN state update rule across layers, and how the RNN output is combined with each backbone layer's hidden states. A brief algorithm pseudocode would suffice.

2. **Remove or substantiate the "theoretical justification" claim.** Either delete contribution item 4 or provide a genuine theoretical analysis (e.g., why operating on the column space of \(\phi\) is sufficient, convergence guarantees, or an interpretation of the correction formulation).

3. **Document the energy measurement protocol** in full: measurement tool, hardware, time granularity, system vs. GPU-only scope, and whether conditions were identical across methods.

4. **Acknowledge the PETL compute-cost reduction honestly.** The paper should recognize that methods like Adapter and LoRA do reduce compute cost meaningfully, and frame READ's advantage as a *further* reduction rather than a binary distinction.

5. **Report standard deviations** for the main results table, especially for comparisons where scores are within 0.1–0.2 points.

---

## Score and Decision

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>