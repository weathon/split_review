Now I have sufficient calibration. Let me synthesize the final review.

## Summary
2-3 sentence summary of the paper's contribution.

The paper introduces the notion of "subgrammars" of context-free grammars (inner and outer) and proves theorems showing that the KL divergence (equivalently, language modeling loss) decomposes recursively over these subgrammars. Empirically, the authors train small transformers on controlled PCFGs and show that (a) all subgrammars are learned in parallel during training, (b) subgrammar pretraining modestly improves internal representation alignment via CKA analysis, and (c) models struggle with deep recursive contexts but not with long non-recursive contexts — a limitation that extends to large LMs.

## Strengths

1. **Novel theoretical framing connecting CFG substructure to LM loss.** The core idea — that the KL divergence of a language model trained on a PCFG should decompose over the grammar's inner subgrammars — is genuinely novel and opens a new direction for studying how neural networks learn hierarchical structure. The formal definitions of inner and outer subgrammars (Definitions 3.3, 3.5) and the unique decomposition DAG (Theorem 4.1) provide a rigorous vocabulary that the community can build on. The connection to Gruska's classical "grammatical levels" is appropriately acknowledged.

2. **Clean experimental separation of depth difficulty from length difficulty in recursive generalization.** Figure 3 convincingly demonstrates that small transformer models fail on deep recursive contexts (error rising to ~0.173 at depth 200) while handling long but shallow contexts with nearly constant low error (~0.017). This controlled disambiguation of depth vs. length is well-designed and clearly presented.

3. **Empirical observation of parallel subgrammar learning.** Figure 1 and Figure 2 show that all subgrammar KL divergences decrease simultaneously from the start of training, with no sequential mastery of simpler before more complex substructures. This is a clean empirical finding about learning dynamics, distinct from the child-language developmental pattern.

4. **Subgrammar pretraining shows measurable effects on representations.** The CKA analysis (Table 1) shows that two-layer transformers pretrained on a subgrammar exhibit 8–22% higher attention-layer alignment across seeds compared to models trained from scratch, and the cosine-similarity analysis (Table 3, described qualitatively) suggests pretrained models better segregate subgrammar from non-subgrammar sequences.

## Weaknesses

### Major

1. **The core mathematical derivation in Section 4.2 is broken as presented.** Equation (4) contains expressions like $\frac{\log P_G(\alpha | \epsilon)}{\log Q_\theta(\alpha | \epsilon)}$, a fraction of two logarithms, which is mathematically nonsensical as a term in a KL divergence decomposition. The KL divergence should decompose into sums of expected log-ratios via the chain rule; what appears in the paper is not a correct derivation. Definition 4.2 uses the notation $D_{\text{KL}}(P_G \parallel Q \mid \neg s)$ where $\neg s$ is undefined and the overall expression is uninterpretable. **Since the paper presents these theorems as its "most important contribution" and the main text derivation is incorrect as written, the core theoretical claim cannot be evaluated from the main text alone.** While the appendix may contain correct proofs (it is stripped from this version), the main text must present a coherent version of the core mathematics. This is a structural flaw that prevents acceptance in the current form.

2. **Empirical validation of the recurrence theorems is qualitative only.** The paper claims that Figure 1 shows a "perfect decomposition" of the total KL into a sum of subgrammar KLs, but provides no quantitative verification: no R², no residual plot, no overlay of the sum of subgrammar curves against the total KL curve, and no numerical error metric. Without this, the plots merely show that all loss curves decrease — which is expected during training. The claim of decomposition is not substantiated quantitatively.

3. **Overclaimed language relative to the evidence.** The abstract and introduction use phrases like "show definitively" and "fundamental theorems" that are disproportionate to the evidence. Specifically, the CKA results show modest absolute increases (0.05–0.06 on a 0–1 scale) — the claim that pretraining "results in internal representations that are more aligned with the grammar's substructure" goes beyond what the CKA evidence supports, since increased CKA across seeds could reflect convergence to a narrower region of weight space rather than qualitatively different "knowledge" of subgrammar structure. The "parallel learning" finding (Corollary 4.7) is stated as a formal result, but it says essentially: if gradient updates on one subgrammar don't hurt performance on others, then all subgrammars improve in parallel. This is a restatement of the independence condition rather than an explanatory mechanism, and the paper acknowledges it is a "pathological, theoretical scenario."

### Minor

4. **Context-insensitivity assumption is only partially reconciled with experimental evidence.** Corollary 4.5 relies on a strong "context insensitivity" assumption. The paper acknowledges this and notes that the deeper-context failure in Section 6 contradicts strict context-insensitivity, but attempts to reconcile it by arguing that deep strings are "rare." This is reasonable but the tension is not fully resolved — the paper does not provide a quantitative analysis of how often the context-insensitivity condition actually holds during training or over the data distribution.

5. **GPT-5.1 anecdotal test adds little.** The paper itself labels the GPT-5.1 arithmetic test as "purely anecdotal" and correctly says it should not be interpreted as direct evidence. This framing is appropriate, but the result (5/5 vs. 2/5 on 5 examples each) is too methodologically weak to support any conclusion and could be omitted without loss.

### Trivial

6. Definition 3.4 says a proper subgrammar is one that "does not contain $G$ itself" — since subgrammars are defined by non-terminal subsets, "contain" is informal here and could be clarified (the intent is simply $G' \neq G$).

7. The curriculum learning section mentions Figure 6 and Table 3 without showing them in the main text (they appear to be in the appendix). Key results from the cosine-similarity analysis are described only qualitatively ("significantly closer," "greater gap") without reported numerical values or statistical tests.

## Nice-to-Haves

- Provide a quantitative validation of the KL decomposition: for a few simple CFGs, compute the total KL and the sum of (scaled) restricted KL terms, and report the residual error or percentage deviation. This would directly substantiate the central theoretical claim.
- Add error bars or confidence intervals to the CKA results and the curriculum learning loss comparisons to strengthen the statistical claims.
- Include a worked-through concrete example of the KL decomposition for a minimal CFG (e.g., the $S \rightarrow x \mid (S \text{ and } S)$ grammar) in the main text to illustrate the theory.

## Removed Points

- *Criticism that "Proper Subgrammar" definition is circular.* The definition is slightly informal but the intent is clear (a strict subgrammar). This is trivial.
- *Criticism about missing related work.* The paper acknowledges Gruska (1971), Allen-Zhu & Li (2023), Bhattamishra et al. (2020), and others. The harsh critic's claim about prior work on nested parentheses failures is already cited (Bhattamishra et al., 2020; Lampinen, 2024).
- *Criticism that "context-insensitivity contradicted by Section 6" without acknowledging the paper's own discussion.* The paper explicitly addresses this tension after Corollary 4.5, noting that deep contexts are rare under the distribution. This criticism was acknowledged but already partially addressed.
- *Criticism that the KL decomposition in Figure 1 lacks any quantitative comparison.* This is retained as a Major weakness because it is valid — the paper says "perfect decomposition" but provides no quantitative evidence.
- *Strength Finder claim about "parallel learning unlike children" being a novel discovery.* This is a genuine empirical observation and is retained.
- *Strength Finder claim about the GPT-5.1 test being a strength.* Removed because the paper correctly labels it as anecdotal and it adds no rigorous evidence.

## Novel Insights

The most interesting structural tension in the paper — and one that neither the authors nor the reviewers fully articulate — is that the paper's theoretical contribution (exact KL decomposition over subgrammars) and its key empirical finding (parallel learning) are in partial tension. The decomposition theorems show that the total loss is exactly the sum of subgrammar losses; this means that optimizing the total loss forces all subgrammar losses to decrease simultaneously, regardless of sequential or parallel dynamics. The "parallel learning" observation is thus not a surprising consequence of the theory but rather a necessary consequence of the loss decomposition combined with gradient-based optimization. The interesting question — which the paper opens but leaves for future work — is whether there exist architecture-dependent effects that could make subgrammar losses *not* decrease simultaneously despite the decomposition (e.g., if shared parameters create interference that slows one subgrammar while another improves). This inversion (the decomposition forces parallel improvement; the mystery is why they don't interfere with each other) is more thought-provoking than the paper's framing of parallel learning as an unexpected discovery.

## Suggestions

1. **Fix the mathematical presentation of Section 4.2.** Provide a clean derivation of the KL decomposition for a concrete CFG example, define the restricted KL divergence with proper notation (e.g., $D_{\text{KL}}^{(A)}(P_G \parallel Q_\theta)$), and state Theorem 4.3 with a brief proof sketch in the main text. The current equation (4) must be corrected.

2. **Add quantitative verification of the recurrence.** For at least one CFG, compute total KL and the sum of (scaled) subgrammar KLs and report the residual. Plot the overlay of total KL and the sum of subgrammar curves.

3. **Calibrate the language.** Replace "show definitively" and "fundamental theorems" with claims commensurate with correlational evidence. The paper is stronger when it describes what it found rather than declaring what it proved.

4. **Reframe the parallel learning claim.** Either provide a mechanistic explanation (e.g., why overparameterization might yield independence) or treat it as a descriptive observation rather than a theorem-grounded finding.

## Score and Decision

**Calibration anchors used:**

**Round 1 (bracketing):**
- uOnElfFuey (3.00), NSBP7HzA5Z (3.00), 7eYmijcuqO (3.00), OW5Gf4cse1 (3.00) — rejected papers; the paper under review has a stronger core contribution and more experimental evidence.
- aWLQTbfFgV (6.25, Accepted), 0pLCDJVVRD (7.00, Accepted), fp77Ln5Hcc (4.50, Rejected), F0Zd3knG9j (5.00, Rejected) — middle band.
- STUGfUz8ob (7.60), n2NidsYDop (8.67), d8w0pmvXbZ (8.00), Tzh6xAJSll (7.60) — strong accepted papers; the paper under review has significantly worse execution.

**Round 2 (narrowing):**
- F0Zd3knG9j (5.00, Rejected) — comparable scope (PCFGs + transformer learning dynamics) and quality level; this paper has a more novel theoretical angle but worse math presentation.
- fp77Ln5Hcc (4.50, Rejected) — similar weakness in confusing presentation and insufficient evidence.
- MRPCIForrE (4.75, Rejected), qGaIMO8dqD (4.67, Rejected) — theoretical papers with nice ideas but significant gaps.

**Round 1 bracket:** The paper sits between the weak anchors (~3.0) and the strong anchors (~7.5–8.7), with an initial bracket of 4.0–6.0.

**Round 2 narrowing:** The paper is comparable to F0Zd3knG9j (5.00) in overall quality — both have interesting ideas about structured learning in transformers on PCFGs, and both have significant issues (math presentation here; novelty questions there). It is slightly better than fp77Ln5Hcc (4.50), which had more confusion and less novel contribution. The paper's core idea is more original than MRPCIForrE (4.75), but the empirical support is weaker than claimed. The paper is meaningfully below aWLQTbfFgV (6.25, Accepted), which had clean, well-supported experiments and a clearly communicated contribution.

**Final score:** 5.0. The paper proposes a genuinely novel perspective on how language models learn hierarchical structure and presents several interesting empirical phenomena. However, the mathematical presentation of the core theoretical contribution is broken in the main text (equation (4) is mathematically incorrect as written, Definition 4.2 is uninterpretable), the central claim of "perfect decomposition" is supported only by qualitative plots, and several claims outrun the evidence. The paper has a real contribution but requires substantial revision.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>