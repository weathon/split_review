## Summary

This paper proposes a self-evolution framework called **SimpleGV** and **RevisionGV**, where a single instruction-tuned language model acts as both generator (producing candidate solutions) and verifier (evaluating their quality) to construct preference data for DPO fine-tuning, requiring no external supervision, reward models, or environment interaction. The key technical contribution is **thresholded majority voting**, which filters noisy self-verification signals into high-confidence preference pairs. The framework is extended with iterative training and curriculum learning, achieving the headline result of 31.0% → 44.8% on Knights-and-Knaves, approaching oracle-supervised performance (46.6%), and the 12B RevisionGV model reaching 52.8% versus a 53.6% oracle ceiling.

---

## Strengths

1. **Self-supervised preference data yields consistent gains across five benchmarks:** Table 1 shows SimpleGV improves over the gemma-3-4b-it base on MATH500 (75.8% → 77.4%), MATHHard (53.7% → 55.1%), and TabMWP (84.5% → 87.4%) without any external labels. The improvements are replicated across both model families (Gemma 3 and Qwen 2.5), reinforcing the generality of the approach.

2. **RevisionGV (12B) nearly closes the gap to oracle supervision:** Table 4 shows the 12B model achieves 52.8% versus 53.6% oracle on KK—an impressively small gap, representing the paper's strongest empirical result. This establishes that multi-turn self-feedback is a particularly powerful signal and that the framework is not far below the supervised ceiling.

3. **Honest and complete ablations with unflattering results included:** The 1B degradation is reported openly (Table 4: base 7.8% vs. SimpleGV τ=0.5: 5.7%, τ=0.6: 5.6%), and oracle results are consistently reported throughout Tables 2–4 as an upper bound. The paper also reports where iterative rounds plateau and where data scaling hurts (Figure 4: TabMWP/KK dip at 40K).

4. **Iterative training and curriculum learning compound gains systematically:** Table 2 shows three rounds of DPO lift KK from 31.0% to 44.1%, and Table 3 shows curriculum ordering (KK23→KK45) reaches 44.8% vs. 41.1% for random mixing, both well-controlled and concrete comparisons.

5. **Cost–performance analysis (Figure 5) provides actionable practitioner guidance:** The heatmaps across generator and verifier budget pairs show that scaling verifier computation is more cost-effective than scaling generator computation—a practical insight with a clear anchor in the presented data.

---

## Weaknesses

### Fatal
None.

### Major

- **Table 1 baseline comparison is confounded by training data and distributional mismatch, undermining the claimed competitive standing against prior methods.** The AZR results for Qwen2.5-7B-Instruct are dramatically below the base model (KK: 5.1% vs. base 18.1%; MATHHard: 32.8% vs. base 49.7%; GSM8K: 84.0% vs. base 90.2%). AZR is a code-centric method evaluated here on general reasoning benchmarks—a distributional mismatch that produces these pathological numbers. The paper says only "we evaluate their released models on the corresponding benchmarks" without explaining or contextualizing the degradation. Meanwhile, SimpleGV trains on **OpenThoughts3** (20K curated reasoning problems), while AZR and other baselines presumably trained on very different, often code-only distributions. Training data composition is not matched across methods, meaning the observed performance gaps could reflect data quality differences rather than methodological superiority. The paper's claim that SimpleGV "achieves performance competitive with previous self-evolution methods" is not well-supported by Table 1 as structured. This is an evidential problem, not a structural one—the method may genuinely be competitive—but the table cannot bear that interpretation as presented.

### Minor

- **The core verify-generate capability gap is assumed, not validated, and the 1B results reveal a real failure regime that is undercharacterized.** Section 3 states "We implicitly assume that a model's ability to verify a candidate is, on average, more reliable than its ability to generate one from scratch" without establishing when this assumption holds or by how much. At 1B, SimpleGV with τ=0.5 and τ=0.6 degrades performance below base (5.7% and 5.6% vs. 7.8%), showing the assumption fails at insufficient model capacity. While the paper notes this ("for smaller models (1B), verifier judgments are noisy"), the framing of "modest improvements" is inaccurate—these are actual regressions at the lower thresholds. More importantly, the paper does not characterize where the capability threshold lies, making it hard to predict when the framework will help or harm in a new setting. Only τ=0.8 recovers to 8.4%, marginally above base, suggesting 1B results are essentially noise-level.

- **The "emergent" framing of easy-to-hard generalization overstates surprise given KK's compositional structure.** The paper calls transfer from 2–3 person KK to 4–8 person KK "emergent easy-to-hard generalization." However, KK problems with 2–3 people are literally simpler sub-problems of the same constraint-satisfaction structure as 8-person problems—they share the same inference rules and logical form. The generalization, while real and quantitatively meaningful (e.g., 4–5 person accuracy: 31.0% → 49.6% after iterative training, Table 2), is not structurally surprising. The word "emergent" carries implication of unexpected cross-task capability, which this particular setting does not provide.

### Trivial

- **The random mixing baseline in Table 3 is not fully specified.** The text says the baseline "uses both easy and hard problems jointly from the start," but does not confirm whether this uses the same total data volume and difficulty distribution as the curriculum condition. This should be one sentence in the experimental setup.

---

## Nice-to-Haves

- A precision-recall audit of the thresholded verifier using oracle labels (which the paper already has for KK) would directly characterize the mechanism: what fraction of the preference pairs generated at each threshold level are actually correct, and how does data coverage change? This would replace the tautological observation "higher threshold → more accurate" with a quantitative characterization of the coverage-precision trade-off that drives training efficacy.

- Adding a single matched-data ablation—SimpleGV trained on the same data type or volume as one of the baselines—would substantially strengthen the comparative claims in Table 1.

- The easy-to-hard generalization claim would be more compelling if demonstrated across structurally distinct tasks rather than only within the compositionally nested KK benchmark.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Harsh Critic – Instruction-tuned confound (Section 2.1):** The critic argues that improvements may partly reflect "activating capabilities baked into the instruction-tuning" rather than genuine self-evolution. This is a generic philosophical concern applicable to virtually all instruction-tuned fine-tuning work and lacks a specific testable prediction. Removed as noise.

- **Harsh Critic – Figure 2 tautology claim:** The critic argues the precision-vs-threshold relationship is "true by construction." While partially correct for intra-line trends, the primary message of Figure 2 is the SimpleGV vs. Base comparison *at each fixed threshold*, which is not tautological—it shows the trained model is a better verifier than the untrained base model at every operating point. The numeric table showing perfectly linear 1% increments is a parser artifact (image OCR), not an actual flaw in the paper. Removed.

- **Harsh Critic – Related work gap on STaR-style approaches:** Per review policy, missing related works are not flagged, as external sources cannot be confirmed. Removed.

- **Strength Finder – "Emergent easy-to-hard generalization" as a core strength:** Demoted. The result is real and quantitatively supported, but the "emergent" framing is overclaimed (see Minor weakness above). The underlying easy-to-hard transfer finding is retained as genuine, but not as a headline strength.

- **Strength Finder – "Simple yet general framework" framing:** This is a generic description of the paper's contribution rather than a specific evidenced strength. Removed as superficial.

---

## Novel Insights

The most genuinely novel observation is the **co-evolution dynamic** shown in Figure 2: after DPO training on self-generated preference data, the model becomes a *better verifier* as well as a better generator (SimpleGV consistently outperforms Base at every threshold), creating a positive feedback loop where the two roles reinforce one another. This verifier co-improvement is not obvious—one might expect preference training on generation quality to have no effect on verification accuracy—and it directly supports the iterative training gains in Table 2. A related insight from Figure 5 and the cost analysis is that verifier scaling is more economical than generator scaling, suggesting the bottleneck in self-evolution at moderate model sizes lies more in signal quality (how reliably can the model judge?) than in sample diversity (how many solutions can it generate?).

---

## Suggestions

1. **Fix Table 1's comparative framing:** Either add a footnote explaining why AZR degrades on general reasoning benchmarks (code-distribution model evaluated out-of-domain), or add a matched-data ablation where all methods operate on the same training prompts. The current comparison misleads the reader about relative method capability.

2. **Validate the verify-generate assumption empirically for KK:** The authors already have oracle labels for KK. Compute the fraction of verifier calls that agree with oracle, broken out by model size (1B/4B/12B) and threshold. Present this as a table alongside Figure 2 to give the assumption concrete empirical grounding and show where the method should not be applied.

3. **Replace "emergent" with more precise language:** Use "easy-to-hard generalization" without the "emergent" modifier, since the KK compositional structure makes this transfer structurally expected. This would avoid reviewers dismissing the real result due to overclaiming.

4. **Specify the random mixing baseline fully in Section 3.5:** State explicitly that it uses the same total number of (easy + hard) preference pairs as the curriculum condition, to pre-empt data-volume confound questions.

---

## Score and Decision

**Originality:** The use of a single model as its own generator-verifier for DPO is not entirely novel in concept, but the thresholded majority voting mechanism, systematic multi-turn revision (RevisionGV), iterative + curriculum extensions, and empirical easy-to-hard analysis together constitute a coherent and meaningful study contribution. Incremental but substantive. **3/5**

**Importance of research question:** Self-improvement without external supervision is a fundamental and timely question for LLM post-training. High importance. **4/5**

**Claims supported:** Core claims (SimpleGV/RevisionGV improve over base model, iterative and curriculum gains, RevisionGV near-oracle at 12B) are well-supported. The comparative claim that the method is "competitive with prior self-evolution methods" is not adequately supported given Table 1's confounds. **3/5**

**Soundness of experiments:** Within the KK benchmark (the main controlled testbed), experiments are sound, ablations are systematic, and multiple seeds are used. Table 1's math benchmarks show promising signals but the comparative baseline setup has the data mismatch issue. **3/5**

**Clarity of writing:** Well-organized with clear definitions, honest limitations section, and interpretable figures. Minor: the "random mixing" baseline is underspecified. **4/5**

**Value to research community:** The cost analysis, scaling insights, and RevisionGV design pattern offer practical value. The systematic documentation of when self-evolution helps (4B+) and hurts (1B) is useful. **4/5**

Overall, the paper presents a solid, honest empirical contribution to an important problem. The core findings are real and the experiments are generally responsible. The main weakness—confounded baseline comparisons in Table 1—is fixable and does not undermine the paper's primary claims about self-improvement over base models. Borderline accept.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>
<subscores>
<originality>3</originality>
<importance>4</importance>
<claims_supported>3</claims_supported>
<soundness>3</soundness>
<clarity>4</clarity>
<community_value>4</community_value>
</subscores>