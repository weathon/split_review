- Decision: Reject
- Avg Score: 4.20
- Scores: 3, 5, 3, 5, 5
Now I have thoroughly read the paper and verified the reviewer claims. Let me synthesize the final review.

---

## Summary

This paper proposes CreDes, a framework combining Causal Relationship Enhancement (CRE) — a loss function that adds Individual Treatment Effect (ITE) terms to cross-entropy — with Dual-End Searching (DES) — a bidirectional search on causal probability trees — to improve LLM performance on long-range reasoning tasks like Blocksworld, GSM8K, and Hanoi Tower. The paper reports strong empirical results, notably non-zero success rates on 12-step Blocksworld where all baselines fail, and large improvements on GSM8K.

## Strengths

1. **Strong empirical results on long-range Blocksworld**: Table 1 shows that across all five base models (Llama-2-7B/13B, Phi-2-7B, Mistral-7B, Mixtral-8x7B), CreDes achieves non-zero success on 8–12 step Blocksworld problems where every baseline (RAP, CoT, RoT, and CRE alone) scores 0.00. For example, on Llama-2-7B, CreDes reaches 0.34 on 12-step vs. 0.00 for all baselines. This is a clear empirical demonstration that the DES decomposition turns unsolvable problems into solvable ones.

2. **Clean ablation between CRE and CreDes**: The Blocksworld table separately reports CRE (without DES) and CreDes (with DES) for the same models and step counts. On 8-step tasks, CRE alone achieves 0.22 but CreDes achieves 0.68 (Llama-2-7B); on 10-step, CRE achieves 0.09 and CreDes achieves 0.51. This isolates DES as the component responsible for handling long-range reasoning.

3. **CRE shows large improvements on GSM8K across multiple models**: The GSM8K table reports CRE achieving 85–93% accuracy across five models, substantially outperforming RAP (39–51%), RoT (32–57%), and CoT (31–49%). While the methodological details for this adaptation are underspecified (see Weaknesses), the raw empirical signal is strong and consistent across architectures.

4. **Time efficiency advantage**: The paper demonstrates (Figure 4) that CreDes maintains near-constant reasoning time as problem length increases, whereas CoT and RAP exhibit steep linear scaling. This simultaneous multi-step reasoning property, if borne out, would be a meaningful practical advantage over cascading single-step methods.

## Weaknesses

### Fatal
None.

### Major

1. **ITE estimation procedure is not specified (CRE)**. The paper claims to estimate the Individual Treatment Effect (ITE) and embed |E(ITE)| and Var(ITE) into the loss (Equation 4), but never specifies how these quantities are actually computed from model outputs during training. Lines 88–92 describe binary variables X (correctness of OSR) and Y (correctness of next state) and discuss intervention conceptually, but no concrete estimator is given. ITE requires potential outcomes under different treatment conditions — the paper does not explain how treatment is assigned, how the counterfactual is obtained, or how E(ITE) and Var(ITE) are computed from a forward pass. Equation 4's claim that this loss equals ln(PPL) is stated without derivation or citation. This is not merely a missing detail: it means the core technical contribution of CRE — the causal regularizer — cannot be implemented or evaluated from the paper as written.

2. **DES uses Euclidean distance over undefined coordinates (DES)**. The distance matrix M_ij in Equation (5) is defined as the Euclidean distance between coordinates (x_i, y_i) of leaf nodes in the head and tail trees. The paper never defines what these coordinates represent. For discrete symbolic planning domains like Blocksworld and Hanoi Tower, states are configurations (e.g., "on(A,B), on(B,table)") that do not naturally live in ℝ². Without specifying how node coordinates are obtained — whether through a learned embedding, a hand-crafted encoding, or something else — the distance computation that drives matching and path selection is underspecified. This undermines reproducibility and raises questions about whether the method can work as described.

3. **GSM8K adaptation details are missing**. CRE is reported (Table GSM8K) to achieve 85–93% on GSM8K — a large improvement over CoT's 31–49%. However, the paper does not explain what constitutes the "state," the "OSR," and the "state transition" in the context of grade-school math word problems. The only description (Section 4.2) says the approach "involves decomposing it into a sequential series of smaller sub-questions," but this does not specify how the causal framework (binary X/Y variables, ITE computation) maps onto math reasoning. Without this, the reader cannot assess whether the GSM8K experiment is a fair application of CRE or a different experimental setup.

4. **Baseline implementations are not described**. The details for CoT, RAP, and RoT implementations are absent: no prompts, hyperparameters, decoding strategies, or verification that the 7B implementations are competitive with published results. Given that RAP on 7B models scores 0.00 on 10–12 step Blocksworld while the original RAP paper uses 70B models, the reader cannot determine whether the baselines are fairly implemented or whether the large gap to CreDes is partly explained by suboptimal baselines.

### Minor

1. **The causal justification for the loss function is not supported**. The paper asserts that ITE measures the causal relationship between OSR and state transition, and that adding |E(ITE)| and Var(ITE) terms to cross-entropy "alleviates causal hallucinations." But no causal identification strategy, no intervention experiments, and no analysis of how these terms change the model's causal behavior are provided. The terms "causal significance" (for the mean) and "causal consistency" (for the variance) are introduced as new labels for standard statistical quantities without justification.

2. **Small training set (80 samples per category)**. The paper states that "for each category, our model is trained on 80 samples without common instructions" (line 54). For a 7B model, 80 training examples is very small. No validation split, no regularization analysis, and no discussion of potential overfitting or memorization are provided. The risk is that the strong short-range results (e.g., 95% on 2-step) reflect pattern matching on a small set rather than genuine causal reasoning.

3. **No statistical significance or error bars**. All results are reported as point estimates without confidence intervals, multiple runs, or any measure of variability. Given the stochastic nature of LLMs and the small training set, the results could be highly variable.

4. **Time efficiency plot lacks description**. Figure 4 is referenced but the axes, units, and absolute numbers are not described in text. No error bars are included.

5. **DES algorithm termination and tree construction details are vague**. The algorithmic description (Algorithm 1) states "Construct T_head and T_tail from State_init and State_goal" without specifying how the trees are built (e.g., how the LLM generates possible actions, how branching is controlled, what the maximum depth is). The 4-step update interval and distance-based selection are sketched but key details (e.g., how "matching" is done) are unspecified.

### Trivial
- "Succcess" typo in the Blocksworld table caption.
- Minor grammatical issues throughout.

## Nice-to-Haves
- Ablation isolating each term in the CRE loss (cross-entropy alone, cross-entropy + |E(ITE)|, cross-entropy + Var(ITE), all three) would strengthen the causal claims.
- Comparison to other decomposition methods (hierarchical planning, means-ends analysis) would contextualize DES.
- Providing the inference prompts and decoding parameters for all baselines would improve reproducibility.
- A description of how the Euclidean coordinates are derived for planning states would resolve the major ambiguity in DES.

## Removed Points
- **"GSM8K results are invalid/implausible and likely due to data contamination or task mismatch"** — This is speculative. The paper provides a table with numbers. While the adaptation is underspecified (a kept weakness), the critic's claim of invalidity goes beyond what can be verified from the page.
- **"The Hanoi Tower table is absent"** — The parser strips tables from the appendix; this is a known artifact, not an author error.
- **"CoT on Blocksworld typically achieves >80% on 2-step tasks, not 50%"** — The paper's own results show Mistral-7B+CoT at 0.84 and Mixtral-8x7B+CoT at 0.81 on 2-step, contradicting the blanket claim. Performance is model-dependent.
- **"Not compared to stronger multi-step prompting techniques (self-consistency, least-to-most)"** — Scope creep; the paper provides a reasonable baseline set (RAP, CoT, RoT) for the domains tested.
- **"The claimed normal distribution for ITE is unsubstantiated (citations may not support this)"** — Speculative about the content of cited references.
- **"The framing sets up a straw-man against CoT"** — Subjective framing critique without concrete evidence.
- **"RAP implementation may be suboptimal"** — Without access to the implementation details, this is speculative.

## Novel Insights
None beyond the paper's own contributions. The two reviews surface a consistent picture: the paper's empirical results are intriguing and suggest real capability, but the methodological exposition is too thin to support the causal claims or enable reproduction. No new structural insight about the method emerges from the reviewer analysis that the paper itself does not already claim or acknowledge.

## Suggestions
1. **Specify the ITE estimation procedure concretely**: provide the exact formula, describe how potential outcomes under treatment/control are obtained from the LLM (e.g., via counterfactual prompting, noise injection, or multiple forward passes), and show how E(ITE) and Var(ITE) are computed during training.
2. **Define the DES node coordinates**: clarify what (x_i, y_i) represents for planning states (e.g., a learned embedding, a hand-crafted feature vector, or the output of a specific encoder).
3. **Describe the GSM8K adaptation**: specify what constitutes the OSR, state, and state transition for math word problems, and how the CRE loss is applied.
4. **Provide baseline implementation details**: include prompts, decoding parameters, and verification that baseline numbers are competitive with published results at the same model scale.
5. **Add error bars or multiple runs**: at minimum, report standard deviations or confidence intervals for key results.
