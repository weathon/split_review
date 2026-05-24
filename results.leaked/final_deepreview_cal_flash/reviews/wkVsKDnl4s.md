Now I have a thorough understanding of the paper. Let me synthesize the review.

**Calibration summary:**

Round 1 brackets:
- Low (<3.5): Weak papers rejected, e.g. IEZjjDX0iC (3.0, reject) on protein LMs — the current paper is clearly stronger
- Middle (3.5–7.5): Papers like SoftHash (5.50, reject), MeToken (5.80, accept), DNABERT-S (5.67, reject) — this range covers papers with solid empirical work but some novelty/framing concerns
- High (>7.5): Strong papers like Tzh6xAJSll (7.60, accept) — clearly stronger than the current paper

Round 2 narrowing:
- DNABERT-2 (6.50, accept) — similar genomics domain, strong benchmarks, some novelty concerns but accepted
- SoftHash (5.50, reject) — some novelty but limited depth
- MeToken (5.80, accept) — solid empirical work, new benchmark, minor concerns

The current paper is stronger than SoftHash (better evaluation, theory contribution) but weaker than DNABERT-2 (framing issue, less practical impact). It's comparable to MeToken but with a more significant framing weakness. I place it at 5.5.

Now writing the final review.

---

Let me also verify the "Metalign" issue more carefully.

From the paper, Table 4:
```
| Database Size | HighClass |  | Metalign |  |
| (genomes) | Throughput (reads/s) | Memory (GB) | Throughput (reads/s) | Memory (GB) |
```

This is the only place "Metalign" appears in the main paper. It's not defined anywhere. This is clearly sloppy.

Let me check the grep results again for "Metalign":
```
341: | Database Size<br>(genomes) | HighClass |  | Metalign |  |
```

Yes, only in Table 4. This should be fixed.

One more thing to verify: the harsh critic said "theoretical analysis appears retroactively fitted." Let me look at the specific claims.

The paper says (line 76): "combined with empirical validation on CAMI II data showing γ ≈ 0.15"
And (line 476-477): "Lemma 7 quantifies concentration under dependencies with empirically validated mixing parameters C ≈ 2.3 and γ ≈ 0.15 (derivation in Appendix C.3)"

So the constants C ≈ 2.3 and γ ≈ 0.15 are estimated from CAMI II data. The critic's point is that these are fitted to the evaluation data. This is a valid concern, but it's standard in applied ML theory to estimate constants from data. The structural results (O(√(V|Y|/n)) convergence, concentration inequalities) don't depend on these specific constants.

I'll keep this as a Minor weakness.

OK, let me produce the final review.Now let me produce the final consolidated review.

## Summary

HighClass proposes a metagenomic classifier that replaces traditional sequence alignment with hash-based token mapping, achieving 4.2× speedup and 68% memory reduction over the state-of-the-art alignment-based method (MetaTrinity) at a cost of ~1.5 pp in F1 (85.1% vs. 86.6% on CAMI II). The paper also contributes a theoretical framework for token-based classification, including generalization bounds via Rademacher complexity, concentration inequalities under α-mixing dependencies, and consistency results.

## Strengths

1. **Clean engineering contribution with convincing efficiency gains.**  
   Table 2 shows HighClass achieves 85.1% F1 (85.7–87.5 CI for MetaTrinity's 86.6%) while cutting runtime from 2.1 h to 0.5 h (4.2×) and memory from 19.3 GB to 6.8 GB (68%). The per-operation breakdown in Table 5 confirms that the three expensive alignment steps (containment search, seeding, chaining) are replaced by cheaper token extraction and hash lookup, directly supporting the claimed O(|𝒯|) complexity.

2. **Rigorous ablation study isolating each component.**  
   Table 3 separately quantifies the contribution of variable-length tokens (+6.8 pp over fixed k-mers), quality weighting (+1.9 pp), and sparsification (68% memory reduction for −0.7 pp F1). The QA-Token + MetaTrinity alignment variant (86.2%) demonstrates that the token vocabulary itself is competitive with MetaTrinity's pipeline, clarifying what each architectural choice contributes.

3. **Theoretical framework for token-based genomic classification.**  
   Sections 4.1–4.3 provide generalization bounds (O(√(V|𝒴|/n))), concentration inequalities under α-mixing with explicit dependency inflation, and consistency guarantees. While the specific constants are empirically fitted, the structural results are non-trivial for this application domain and go beyond what comparable systems (Kraken2, Centrifuge, MetaTrinity) provide.

4. **Statistical rigor in evaluation.**  
   Results are reported with 95% bootstrap confidence intervals, Wilcoxon signed-rank tests with Holm-Bonferroni correction, and Cohen's d effect sizes (d = 5.2 for runtime, d = −0.9 for accuracy). This is more thorough than typical metagenomic classifier evaluations.

5. **Scalability demonstration across database sizes.**  
   Table 4 shows HighClass maintains >689 k reads/s even at 10,000 genomes (124.5 GB), while the alignment baseline runs out of memory at that scale, demonstrating the approach is not limited to small benchmarks.

## Weaknesses

### Fatal
None.

### Major

1. **Unexplained discrepancy between QA-Token's 91.7% F1 and HighClass's 85.1% F1.**  
   The paper states (Section 2.1) that QA-Token "achieves 0.917 taxonomic F1 on CAMI II" and that HighClass adopts its vocabularies. Yet HighClass itself achieves only 85.1% on the same benchmark. The paper frames "near-parity with state-of-the-art" by comparing to MetaTrinity's 86.6%, but the relevant upper bound for a method *using QA-Token's tokenizer* is 91.7%, not 86.6%. The paper never explains what pipeline produced QA-Token's 0.917, why that pipeline is not used here, or whether QA-Token's 0.917 came from a fundamentally different (and presumably much more expensive) classifier. This omission makes the accuracy framing misleading: a reader cannot tell whether HighClass's 85.1% represents a genuine advance in the efficiency–accuracy Pareto frontier or simply a degraded version of an existing high-accuracy pipeline. The authors should directly address this gap — e.g., by stating that QA-Token's 0.917 was achieved with a neural network classifier whose computational cost is prohibitive at scale, and positioning HighClass explicitly as a lightweight alternative that trades accuracy for speed relative to *that* baseline, not just MetaTrinity.

### Minor

2. **Theoretical constants estimated from the same evaluation data.**  
   The parameters C ≈ 2.3 and γ ≈ 0.15, the variance inflation factor (≈31.7), and the excess risk bound (≈0.021) are all "empirically validated" on CAMI II — the same dataset used for the main evaluation. This makes the theoretical analysis more descriptive than predictive. While the structural results (O(√(V|𝒴|/n)) rate, concentration inequalities) do not depend on these constants, the paper would be stronger if it validated the bound on a held-out dataset (e.g., CAMI I or HMP) and checked whether the predicted excess risk holds on unseen data.

3. **Undefined baseline "Metalign" in Table 4.**  
   Table 4 compares HighClass against "Metalign" for scalability, but "Metalign" is never defined, cited, or otherwise introduced anywhere in the paper. It does not appear among the primary baselines (MetaTrinity, Kraken2, Centrifuge). This is a clear oversight that must be corrected — either by removing the column or properly referencing what Metalign is and why it is compared.

4. **Sparsification component description is thin.**  
   The paper states it "employ[s] gradient-based importance scoring" using "pre-computed importance masks" but does not clearly specify on what data these masks are learned, whether they were trained on the same CAMI II data (risking leakage), or what the training procedure was. The details may appear in the (stripped) appendix, but the main text should at minimum state the provenance of the masks.

### Trivial
None beyond those listed above.

## Nice-to-Haves

- **Validate theoretical predictions on a second dataset.** Running the same analysis on CAMI I or HMP data and reporting whether the excess risk bound and mixing parameters transfer would substantially strengthen the theory contribution.
- **Benchmark against QA-Token's original classification pipeline** if it can be reproduced, or at minimum discuss its computational cost to substantiate the claim that HighClass's efficiency gains justify the accuracy drop.
- **Clarify whether the sparsification masks are learned from scratch or adopted from Alser et al. (2024)** and whether any fine-tuning was performed on CAMI II data.

## Removed Points

These points from the reviewers are flagged for removal; treat them with caution.

- **From Harsh Critic: "Ablation study contradicts the paper's own attribution of credit."**  
  *Reason for removal:* The critic claims that QA-Token+MetaTrinity alignment (86.2%) being close to MetaTrinity (86.6%) means "the QA-Token vocabulary itself provides no accuracy benefit." This misreads the evidence: the ablation clearly shows tokens provide +6.8 pp over fixed k-mers (78.3% → 85.1%), and the 86.2% vs 86.6% comparison shows that the token vocabulary is *competitive* with MetaTrinity's internal pipeline, not that it provides no benefit. The critic also conflates the token vocabulary with the hash-based mapping — the paper frames hash mapping (not the vocabulary) as the speed enabler, which is consistent with the evidence.

- **From Harsh Critic: "Theoretical analysis appears retroactively fitted" presented as a fatal/gap-level weakness.**  
  *Reason for demotion:* The constants are indeed estimated from CAMI II data, but this is acknowledged ("empirically validated") and the structural results (convergence rate, concentration form) do not depend on the specific constants. This is a standard practice in applied learning theory. The criticism is valid in spirit (it would be stronger with held-out validation) but does not approach a fatal flaw. Demoted to Minor.

- **From Harsh Critic: "MetaTrinity is the wrong comparison" framing.**  
  *Reason for partial removal:* The critic's claim that the paper must benchmark against QA-Token's pipeline is a reasonable suggestion (preserved in Major 1 and Nice-to-Haves), but the assertion that this "invalidates" the paper's central claims is too strong. HighClass's speed and memory gains are measured independently of this comparison; the issue is only about how accuracy is framed, not about the validity of the efficiency results.

- **From Strength Finder: Generic strengths about "important problem" and "timely contribution."**  
  *Reason for removal:* These add no specific evidence. I have retained only strengths that cite concrete data, tables, or derivations.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Reframe the accuracy narrative.** Acknowledge QA-Token's 0.917 F1 result directly, explain what classification pipeline produced it and why it is not directly comparable (e.g., it likely uses a neural network classifier that is orders of magnitude slower), and position HighClass explicitly on the speed–accuracy Pareto frontier rather than as a "near‑SOTA" method. This would turn a weakness into a more honest and actually stronger contribution.

2. **Define "Metalign" or remove it.** Table 4 either needs a proper citation and description of Metalign, or the column should be removed.

3. **Add a held‑out theoretical validation.** Run the mixing analysis on a second independent dataset (e.g., CAMI I or HMP) and report whether the predicted excess-risk bound holds, to demonstrate that the theory is predictive rather than descriptive.

4. **Clarify sparsification mask provenance.** Explicitly state (even in a single sentence) whether the importance masks were learned on CAMI II training data, on a separate dataset, or adopted without modification from Alser et al. (2024).

## Score and Decision

**Round 1 bracketing.** Retrieved anchors in three bands:
- Weak band (avg < 3.5): IEZjjDX0iC (3.00, reject), GOjr2Ms5ID (3.25, reject), MGceYYNvXp (1.50, reject), n7iwmPacDt (3.00, reject) — the current paper is clearly stronger than these.
- Middle band (3.5 < avg < 7.5): noUF58SMra / MeToken (5.80, accept), cNwugejbW6 / SoftHash (5.50, reject), vBw8JGBJWj (4.33, accept), 9klRFLY2TT / DNABERT-S (5.67, reject) — this is the relevant range.
- Strong band (avg > 7.5): STUGfUz8ob (7.60, accept), Tzh6xAJSll (7.60, accept) — the current paper is clearly weaker than these.
**Initial bracket: 4.5–6.5.**

**Round 2 narrowing (inside bracket).** Retrieved additional anchors:
- 9klRFLY2TT / DNABERT-S (5.67, reject) — comparable evaluation quality but HighClass has more theoretical depth and a clearer efficiency story; however DNABERT-S has a cleaner framing.
- oMLQB4EZE1 / DNABERT-2 (6.50, accept) — stronger practical impact (foundation model), cleaner framing, but less theoretical contribution than HighClass.
- Q6PAnqYVpo (5.67, accept) — solid pattern-matching system with similar methodological contribution level.
- B5iOSxM2I0 / Tokenization Foundations (6.50, accept) — stronger theoretical contribution but in a different domain.

Comparing against these: the current paper is weaker than DNABERT-2 (6.50) due to the QA-Token framing issue and the theory constants being fitted on evaluation data. It is comparable to MeToken (5.80) and DNABERT-S (5.67) in overall quality. The framing issue is significant enough to prevent a score at the top of the bracket but not severe enough to drop it to the bottom. I therefore place it at **5.5**.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>