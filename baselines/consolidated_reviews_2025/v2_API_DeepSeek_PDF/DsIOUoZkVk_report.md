## Summary
# Final Review Report

## Summary

This paper presents a theoretical analysis of contrastive learning for cross-modal alignment when modalities are not directly paired in training data (e.g., aligning audio and text via an intermediate image modality). The authors prove that under three assumptions — (A1) conditional independence of target modalities given an intermediate "bridge" modality, (A2) InfoNCE-trained representations encode density ratios, and (A3) representations are uniformly distributed on the hypersphere (or Gaussian for unnormalized case) — the dot product (or L2 distance) between unpaired representations is a monotonic function of the true likelihood ratio. This result, termed the "Law of the Unconscious Contrastive Learner," provides theoretical justification for a heuristic widely used in multimodal contrastive learning systems such as ImageBind and LanguageBind. The paper also proposes a Monte Carlo LogSumExp (LSE) method that replaces costly integrals over the intermediate modality and works under weaker assumptions (A1-A2 only). Experiments on synthetic data, CLIP/CLAP models on AudioSet, and a language-conditioned reinforcement learning navigation task validate the theory and demonstrate practical applications.

**Core strengths:** The paper addresses an important and timely question — whether and why cross-modal alignment works without direct training pairs. The theoretical framing (Lemma 1 linking contrastive representations to Bayesian marginalization) is elegant and builds insightfully on prior geometric and probabilistic understanding of contrastive learning. The practical LSE algorithm is a useful contribution that can be applied to combine pre-trained models without retraining.

**Core weaknesses:** (1) The main theoretical result (Lemma 2) relies on a restrictive set of assumptions that are frequently violated in practice, limiting its scope. (2) Several experimental claims are overstated or lack proper controls. (3) The LSE method is presented without practical guidance on sample sizes or bias. (4) The bridging-modalities scenario assumes compatible intermediate representation spaces, a significant practical barrier that is not addressed. (5) The RL experiment has a confound between marginalization and information access. Novelty/comparison conclusions are deferred due to external literature verification being unavailable in this run.

## Strengths
**S1 — Important and timely research question.** The paper addresses a fundamental gap in multimodal contrastive learning: why does the "plug-n-play" heuristic of directly comparing unpaired modality representations work? This question is central to modern multimodal systems (CLIP, CLAP, ImageBind, LanguageBind), yet prior work had not provided a rigorous theoretical account. The paper's framing of this as a probabilistic marginalization problem is insightful and well-motivated.

**S2 — Elegant theoretical connection.** The derivation linking contrastive representations to Bayesian marginalization over an intermediate modality (Lemma 1) is a clean and non-trivial insight. The observation that the "direct comparison" heuristic corresponds to a specific closed-form integral under the uniform-marginal assumption connects contrastive learning to probabilistic graphical model message passing in a novel way. This theoretical scaffolding is the paper's strongest intellectual contribution.

**S3 — Practical Monte Carlo alternative.** The LSE method (Section 5) is a pragmatic contribution that addresses the failure cases of the direct heuristic. By requiring only Assumptions 1-2 (not the restrictive Assumption 3), it provides a broadly applicable fallback. The algorithm is simple to implement (a single LogSumExp operation on precomputed embeddings) and the paper demonstrates its utility in multiple settings.

**S4 — Real-world validation on diverse tasks.** The paper validates its theory across multiple settings: controlled synthetic data, real-world multimodal benchmarks (AudioSet with CLIP/CLAP/LanguageBind), and a downstream application (language-conditioned RL). This multi-setting evaluation strengthens the practical relevance of the theoretical results.

**S5 — Honest limitation discussion.** The paper acknowledges that it does not provide a final decision rule for when to use direct comparison vs. LSE, which is an appropriate boundary for the current work. The self-awareness about the gap between theory and practice is commendable.

## Weaknesses
**W1 — Restrictive assumptions limit practical scope of the main theoretical result (Severity: Major).** Lemma 2 (the "Law") requires all three assumptions simultaneously: conditional independence (A1), InfoNCE-to-density-ratio (A2), and uniform hyperspherical marginals (A3). The paper's own experiments (Fig 2b) show that Assumption 3 is violated for the unnormalized dot product critic — one of the most commonly used similarity functions in contrastive learning (e.g., CLIP). This means the "Law" that the paper is named after does not hold in many realistic settings. The abstract and introduction do not sufficiently qualify this limitation, potentially misleading readers about the scope of the theoretical guarantee.

**W2 — Synthetic experiments are self-fulfilling (Severity: Minor).** The synthetic data generation uses a linear Gaussian model that is designed to satisfy Assumptions 1-3 by construction. While this provides a controlled verification of sufficiency, it does not test robustness under real-world distribution shifts or non-linear relationships. The paper's claim that experiments "validate" the theory would be stronger with a non-Gaussian or non-linear synthetic variant that probes boundary conditions.

**W3 — LSE method lacks practical implementation guidance (Severity: Major).** Section 5 presents the LSE method without guidance on (a) how many Monte Carlo samples are needed in practice, (b) the bias introduced by taking the log of a Monte Carlo estimate (LogSumExp bias via Jensen's inequality), and (c) computational cost scaling. Appendix C.1 reveals that up to 500,000 samples are needed for convergence on LanguageBind, which is computationally expensive and not discussed in the main text. This undermines the practical utility claimed for the method.

**W4 — LanguageBind as "validation" of the Law is circular (Severity: Major).** Section 6.2.1 claims that "Direct evaluation with LanguageBind achieves a 70% recall... which further empirically validates our 'Law'." However, LanguageBind was explicitly designed and trained to enable direct cross-modal comparison through a shared language embedding space. Its performance is a consequence of its training objective, not an independent test of the paper's theoretical claims. This reasoning is tautological.

**W5 — Bridging pre-trained models assumes compatible intermediate spaces (Severity: Major).** Section 6.2 describes a scenario where two independently trained models (e.g., ϕA↔ϕB1 from one repository and ϕB2↔ϕC from another) are combined. The LSE method requires a shared ϕB distribution, but the paper never addresses how to align ϕB1 and ϕB2 when they have different architectures, dimensionalities, or training distributions. The synthetic experiment sidesteps this by using matched B representations.

**W6 — RL experiment confound: unequal information access (Severity: Major).** The RL experiment compares the LSE method (which uses a distribution over future states sf) against a direct baseline (which uses only the language embedding ϕC(ℓ)). The LSE method's superiority may be partly due to having access to more information (the full sf distribution) rather than the marginalization property per se. No controlled ablation isolates the marginalization benefit.

**W7 — Uniformity test has low statistical power (Severity: Major).** Section 6.2.2 tests Assumption 3 using a KS test on ~600 AudioSet ontology descriptions in high-dimensional spaces (d=512). The p-values (CLIP: 0.0877, CLAP: 0.1788) do not reject uniformity, but the test has very low power in high dimensions with modest sample sizes. The paper overstates the conclusion that "Assumption 3 fares well in complex real-world settings."

**W8 — Formula inconsistency in Lemma 2 proof (Severity: Minor).** The final step of Lemma 2's proof contains a notational error: $\kappa = \sqrt{2 + \phi(A)^\top \phi(B)}$ references $\phi(B)$ where $\phi(C)$ is intended, and the factor of 2 inside the square root is missing ($\kappa = \sqrt{2 + 2\phi(A)^\top \phi(C)}$ is the correct expression). While the final result is not affected (the error appears to be typographical), it creates confusion for readers.

**W9 — Conclusion too brief and limitation too vague (Severity: Minor).** The conclusion does not enumerate validated findings or provide a practical decision rule. The limitation paragraph states only that the paper "does not provide the final word" without specifying what evidence is missing.

## Key Issues
### Ranked Error Board (Top-5 Defects by Severity | Research-Value Impact | Validity Risk | Fixability | Confidence)

| Rank | Issue | Severity | Res.Value Impact | Validity Risk | Fixability | Confidence |
|------|-------|----------|-----------------|--------------|------------|------------|
| 1 | Direct comparison "Law" relies on assumptions frequently violated (W1) | Major | High | High | Partial (bounded claims) | High |
| 2 | LSE method lacks sample-size guidance and log-bias analysis (W3) | Major | High | Medium | Easy (add text) | High |
| 3 | Bridging models assumes compatible intermediate spaces (W5) | Major | High | High | Partial (requires additional alignment) | High |
| 4 | RL experiment has information-access confound (W6) | Major | Medium | Medium | Easy (add ablation) | High |
| 5 | LanguageBind validation is circular (W4) | Major | Medium | Low | Easy (rewrite claim) | High |

### Summary of Core Tensions

The paper has a fundamental tension between its theoretical ambition and its practical claims. The "Law" (Lemma 2) is the paper's most striking result but requires the most restrictive assumptions (all three including uniform marginals). When those assumptions are violated — which the paper itself demonstrates for the dot product critic — the "Law" does not hold. The LSE method, which requires fewer assumptions, is presented as a practical alternative but is not given the same prominence. The paper's strongest conceptual contribution (Lemma 1 connecting contrastive representations to Bayesian integration) is somewhat overshadowed by the catchy "Law" framing, when it is arguably the more robust and practically useful result.

A second tension is between the claimed generality of the approach and the specific conditions under which it is tested. The synthetic experiments are designed to satisfy the assumptions, the CLIP/CLAP experiments require a shared ontology for the intermediate language space, and the RL experiment does not control for information access. Each experiment individually supports the theory, but the accumulation of caveats limits the paper's overall generalizability claim.

## Actionable Suggestions
### Suggestion 1 (Must) — Bound claim scope in Abstract and Introduction
**Location:** Page 1 - Abstract, Page 1 - Introduction paragraph 1
**Action:** Add explicit qualifiers that the "Law" requires all three assumptions, and that these are frequently violated in practice.
**Revised abstract (last two sentences):**
"Starting with the proper Bayesian approach of integrating out intermediate modalities, we show that directly comparing the representations of unpaired modalities can recover the same likelihood ratio **when the representations satisfy specific distributional properties (uniform on the hypersphere or isotropic Gaussian). When these properties are violated — as can happen in practice — we provide a Monte Carlo alternative that requires fewer assumptions.** "
**Expected benefit:** Prevents over-interpretation of the theoretical guarantee.

### Suggestion 2 (Must) — Add sample-size guidance and log-bias discussion for LSE
**Location:** Page 6 - Section 5
**Action:** Add 2-3 sentences between the current paragraph and the LogSumExp formula:
"In practice, we recommend at least $10^4$ Monte Carlo samples for stable estimates, though convergence may be slower in high-dimensional spaces (see Appendix C.1). A caveat is that taking the logarithm of a Monte Carlo estimate (the LogSumExp) introduces bias for finite $N$ due to Jensen's inequality; this bias decays as $O(1/N)$ and is negligible for $N \gtrsim 10^4$ in our experiments."
**Expected benefit:** Makes the LSE method immediately usable by practitioners.

### Suggestion 3 (Must) — Fix formula typo in Lemma 2 proof
**Location:** Page 6 - Lemma 2 proof, final line
**Action:** Replace $\frac{1}{C_p(\sqrt{2 + \phi(A)^\top \phi(B)})}$ with $\frac{1}{C_p(\sqrt{2 + 2\phi(A)^\top \phi(C)})}$.
**Expected benefit:** Removes reader confusion and maintains mathematical correctness.

### Suggestion 4 (Must) — Clarify LanguageBind validation
**Location:** Page 9 - Section 6.2.1
**Action:** Replace "which further empirically validates our 'Law'" with:
"This result is **consistent with** our theoretical analysis, though LanguageBind was explicitly designed and trained to enable direct cross-modal comparison, so its performance does not constitute an independent test of our framework."
**Expected benefit:** Avoids circular reasoning and maintains scientific honesty.

### Suggestion 5 (Must) — Address compatible intermediate spaces for bridging models
**Location:** Page 8 - Section 6.2
**Action:** Add a paragraph after the black-box API description:
"A practical challenge arises when the two pre-trained models use different intermediate encoders ($\phi_{B1}$ and $\phi_{B2}$), producing incompatible embeddings. Our method requires a shared representation space for the B modality. When embeddings are dimensionally compatible, a linear alignment can be learned from a small set of overlapping B samples; when they are not (e.g., proprietary APIs), only score-level combination is feasible. We leave systematic handling of incompatible intermediate spaces to future work."
**Expected benefit:** Clarifies the scope of the bridging claim and provides a practical path forward.

### Suggestion 6 (Must) — Add control ablation for RL experiment
**Location:** Page 10 - Section 6.3
**Action:** Add a "Direct+Average" baseline: $\max_a \frac{1}{N} \sum_{i} \phi_A(s,a)^\top \phi_B(s_{f_i})$ compared against $\phi_C(\ell)$. Report whether this narrows the gap to the LSE method.
**Expected benefit:** Isolates the marginalization benefit from the information-access confound.

### Suggestion 7 (Nice-to-have) — Strengthen uniformity test
**Location:** Page 9 - Section 6.2.2
**Action:** (a) Add a test on a more diverse language corpus (e.g., Wikipedia captions). (b) Add a note: "The KS test has limited power in high dimensions with ~600 samples; results should be interpreted as not rejecting uniformity rather than confirming it."
**Expected benefit:** Makes the statistical claim more defensible.

### Suggestion 8 (Nice-to-have) — Expand conclusion with practical decision rule
**Location:** Page 10 - Section 7
**Action:** Add a paragraph:
**Practical recommendation:** Use direct comparison when (a) representations are L2-normalized with dot-product or L2 critic, (b) the marginal distribution is approximately uniform (test via KS or similar), and (c) conditional independence (Assumption 1) is plausible. Otherwise, use the LSE method, ensuring sufficient Monte Carlo samples ($N \geq 10^4$)."
**Expected benefit:** Gives practitioners an evidence-grounded decision rule.

## Storyline Options + Writing Outlines
### Current Storyline Analysis

The current storyline follows this structure:
1. Motivation: Contrastive learning enables "plug-n-play" modality swapping (Page 1)
2. Two key ideas: probabilistic interpretation + marginal distribution assumptions (Page 1)
3. Related work (Page 2)
4. Problem statement and assumptions (Pages 3-4)
5. Lemma 1: Bayesian marginalization over intermediate modality (Page 4)
6. Triangle inequality intuition (Page 5)
7. Lemma 2: The "Law" — closed form under Assumption 3 (Pages 5-6)
8. Lemma 3: Extension to unnormalized/Gaussian (Page 6)
9. LSE practical algorithm (Page 6)
10. Experiments (Pages 7-10)
11. Conclusion (Page 10)

**Problem:** The paper front-loads the "Law" (Lemma 2) as the headline result, but this result requires the most assumptions and is frequently violated. The more practical contribution (LSE, Lemma 1) appears later and receives less emphasis. The introduction does not clearly separate the two contributions or explain when each applies.

### Recommended Alternative Storyline (Option A — "Two-Contributions" Structure)

This structure gives equal billing to the two contributions and clearly separates their assumption requirements:

1. **P1: Problem and motivation** (same as current, but sharper)
2. **P2: The gap** — formalize what "alignment" means probabilistically; state the density ratio target
3. **P3: Result 1 — The Bayesian marginalization view** (Lemma 1): no distributional assumptions, but requires Monte Carlo sampling
4. **P4: Result 2 — The "Law"** (Lemma 2): closed-form when Assumption 3 holds
5. **P5: Practical recommendation** — summary of when each result applies
6. **P6: Contributions** — bullet list

### Alternative Storyline (Option B — "Assumptions-First" Structure)

This structure organizes around the three assumptions, making it clear which are necessary for each result:

1. **P1: Motivation** (same)
2. **P2: What we need to assume** — list Assumptions 1-3 upfront
3. **P3: What we can prove with A1+A2 only** (Lemma 1 + LSE)
4. **P4: What we can prove with A1+A2+A3** (Lemma 2: the "Law")
5. **P5: Contributions and relation to prior work**

### Recommended Choice: Option A

Option A best serves the paper because it gives proper prominence to the more practical LSE contribution while still highlighting the elegant theoretical result.

### Abstract Outline (Recommended Revision)

- **S1 (Problem + Domain):** "Contrastive learning is widely used to align representations across modalities, but it is often applied to modality pairs (e.g., image↔text, audio↔text) that do not share direct training pairs."
- **S2 (Challenge):** "A common heuristic is to directly compare representations from unpaired modalities (e.g., image↔audio), implicitly assuming that this comparison preserves the correct probabilistic relationship. It has been unclear when this heuristic is justified."
- **S3 (Method/Theory):** "We prove that, under specific assumptions about the learned representation distributions (uniform on the hypersphere or isotropic Gaussian), the direct heuristic indeed recovers the correct density ratio. When these assumptions are violated, we provide a Monte Carlo algorithm that requires fewer assumptions and remains valid."
- **S4 (Applications):** "We demonstrate the utility of our framework in two settings: bridging pre-trained CLIP and CLAP models for zero-shot audio-visual retrieval, and handling ambiguous language instructions in reinforcement learning."
- **S5 (Key Result + Bound):** "On AudioSet, our Monte Carlo method achieves 62% Recall@10 using only pre-trained model APIs, while direct comparison achieves 14%."

### Introduction Outline (Recommended 6-Paragraph Structure)

**Paragraph 1 (Problem):** "Multimodal contrastive learning has been remarkably successful, producing models like CLIP, CLAP, and LanguageBind that can align diverse modalities. A key practical appeal is the ability to swap modalities — using (say) a language embedding where an image embedding was expected — without retraining. But the principle underlying this 'plug-n-play' capability remains poorly understood."

**Paragraph 2 (Gap):** "Specifically, if we train encoders on pairs A↔B and B↔C, does the similarity score ϕ(A)⊤ϕ(C) recover the true density ratio p(C|A)/p(C)? Prior work has not provided a rigorous answer to this question, nor has it identified conditions under which the heuristic fails."

**Paragraph 3 (Contribution 1 — Broad assumptions):** "Our first result (Lemma 1) shows that, under only the assumptions that (i) A and C are conditionally independent given B, and (ii) the contrastive encoders encode density ratios, the true density ratio can be expressed as an expectation over B's representations. This leads to a practical Monte Carlo algorithm (Section 5) that works under broad conditions."

**Paragraph 4 (Contribution 2 — Stronger assumptions, closed form):** "Our second result (Lemma 2) shows that when the representations additionally satisfy a uniform distribution on the hypersphere (Assumption 3), this expectation has a closed form: the density ratio is a monotonic function of the dot product between ϕ(A) and ϕ(C). This justifies the direct comparison heuristic — but only when the distributional assumption holds."

**Paragraph 5 (Practical recommendation and applications):** "We validate our theory on synthetic data, on real-world audio-visual retrieval using CLIP and CLAP, and on a language-conditioned navigation task. Our results suggest a clear practical guideline: use the LSE method unless one can verify Assumption 3 on the target data."

**Paragraph 6 (Contributions statement):** "In summary, this paper provides (a) a Bayesian formalization of cross-modal contrastive alignment, (b) a closed-form justification of the direct comparison heuristic under specific conditions, and (c) a practical algorithm that relaxes those conditions."

## Priority Revision Plan
### P0 (Must do before resubmission)

| # | Task | Location | Effort | Impact | Effort/Impact |
|---|------|----------|--------|--------|---------------|
| P0.1 | Bound claim scope in Abstract & Introduction | Pages 1 | Low (text edit) | High (prevents over-claim) | ★★★★★ |
| P0.2 | Add LSE sample-size guidance + log-bias discussion | Page 6, Section 5 | Low (add 2-3 sentences) | High (makes method usable) | ★★★★★ |
| P0.3 | Fix Lemma 2 proof typo | Page 6 | Trivial | Medium (avoids confusion) | ★★★★★ |
| P0.4 | Clarify LanguageBind validation is not independent | Page 9, Section 6.2.1 | Low (rewrite 1 sentence) | High (avoids circular reasoning) | ★★★★★ |
| P0.5 | Add compatible-intermediate-space discussion | Page 8, Section 6.2 | Medium (add 3-5 sentences) | High (clarifies practical scope) | ★★★★☆ |
| P0.6 | Add RL control ablation (Direct+Average) | Page 10, Section 6.3 | High (extra experiment) | High (resolves confound) | ★★★☆☆ |

### P1 (Should do for strong revision)

| # | Task | Location | Effort | Impact | Effort/Impact |
|---|------|----------|--------|--------|---------------|
| P1.1 | Expand conclusion with practical decision rule | Page 10, Section 7 | Low (add 4-5 sentences) | Medium (helps practitioners) | ★★★★☆ |
| P1.2 | Strengthen uniformity test with more data | Page 9, Section 6.2.2 | Medium (extra computation) | Medium (stronger statistical claim) | ★★★☆☆ |
| P1.3 | Add non-linear synthetic variant | Page 7, Section 6.1 | Medium (new data generation) | Medium (tests assumption robustness) | ★★★☆☆ |

### P2 (Nice-to-have improvements)

| # | Task | Location | Effort | Impact | Effort/Impact |
|---|------|----------|--------|--------|---------------|
| P2.1 | Reorganize Introduction per Option A | Pages 1-2 | Medium (structural rewrite) | Medium (clearer narrative) | ★★★☆☆ |
| P2.2 | Restructure Related Work as thematic comparison | Page 2 | Low (reorganize text) | Medium (better positioning) | ★★★☆☆ |
| P2.3 | Add separate-trainers assumption note | Page 3, Section 3.1 | Low (add 1-2 sentences) | Low (clarifying) | ★★☆☆☆ |

### ASCII Diagram — Revision Strategy Roadmap

```text
[P0.1: Bound claims in Abstract/Intro]
    -> Prevents over-interpretation of "Law"
    -> Expected: readers understand assumption-dependence
[P0.2: LSE sample-size guidance + log-bias]
    -> Makes LSE method immediately usable
    -> Expected: practitioners can reproduce without guesswork
[P0.3: Fix Lemma 2 formula typo]
    -> Removes reader confusion
[P0.4: Clarify LanguageBind is not independent validation]
    -> Eliminates circular reasoning
[P0.5: Add compatible-intermediate-space discussion]
    -> Clarifies bridging limitation
    -> Expected: honest scope, practical suggestion for alignment
[P0.6: RL Direct+Average ablation]
    -> Isolates marginalization benefit from information confound
    -> Expected: either confirms LSE's unique advantage or reframes claim

P1.1: Expand conclusion -> practical decision rule
P1.2: Stronger uniformity test
P1.3: Non-linear synthetic variant

P2.1: Reorganize Introduction
P2.2: Thematic Related Work
P2.3: Joint-trainer assumption note
```

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory

| Exp ID | Objective/Hypothesis | Setup (data/split/protocol/baselines) | Metrics | Main Outcome | Claim Supported | Current Limitation |
|--------|---------------------|---------------------------------------|---------|-------------|----------------|-------------------|
| E1 | Test "Law" with 3 critic functions on synthetic data (Section 6.1.1) | Linear Gaussian synthetic data, 5000 train/1000 val pairs, 20 random seeds, 3 critics (L2, dot product, normalized dot product) | Recall@1 | L2 critic: all methods work. Dot product: Direct fails (violates A3). Norm. dot: Direct works despite A2 violation | Sufficiency (not necessity) of assumptions | Synthetic data is linear Gaussian by design; does not test non-linear or non-Gaussian real-world violations |
| E2 | Bridging pre-trained models with LSE on synthetic data (Section 6.2) | Same synthetic setup, two separately trained critics ϕA↔ϕB1 and ϕB2↔ϕC with L2 critic | Recall@1 | LSE approaches oracle accuracy; Direct = chance | LSE enables cross-model bridging | Assumes compatible ϕB1/ϕB2 spaces (same dim, distribution) |
| E3 | Audio-visual retrieval on AudioSet via CLIP/CLAP (Section 6.2.1) | AudioSet with CLIP (image-text) and CLAP (audio-text), ~600 AudioSet ontology descriptions for intermediate language | Recall@10 | LSE: 62%, Direct: 14%, LanguageBind: 70% | LSE connects disjoint pre-trained models | Limited ontology size (~600), LSE still 8% below LanguageBind |
| E4 | LanguageBind direct evaluation on AudioSet (Section 6.2.1) | AudioSet with LanguageBind encoders | Recall@10 | Direct: 70%, LSE: 58% (converges to 70% with 500K samples, Appendix C.1) | "Validates the Law" (circular — see W4) | LanguageBind was trained for direct comparison |
| E5 | Uniformity test (Section 6.2.2) | AudioSet ontology language embeddings from CLIP/CLAP vs uniform hypersphere via KS test | p-value | CLIP p=0.0877, CLAP p=0.1788 — both fail to reject uniformity | Assumption 3 not rejected | Low power (~600 samples, high dim), narrow ontology corpus |
| E6 | Language-conditioned RL navigation (Section 6.3) | PointMaze variants with ambiguous language annotations, contrastive RL for (s,a)↔sf and sf↔ℓ alignments | Success rate | LSE improves 20-30% over Direct | LSE handles ambiguous language better | Confound: LSE has access to sf distribution, Direct does not |
| E7 | Scaling of LSE samples (Appendix C.1) | ImageBind/LanguageBind on AudioSet, vary N from 1 to 500,000 | Recall@1 | LSE converges to Direct as N→∞ | Performance gap = sampling, not theoretical limitation | Only tested on AudioSet data |
| E8 | Modality swapping experiments (Appendix C.2) | Image↔Language via audio (ImageBind+CLAP), Audio↔Language via images (ImageBind+CLIP) | Recall@1 | LSE matches Direct within 1-3% | LogSumExp works with various intermediate modalities | Small evaluation set (25 candidates) |

### Research-Theme Gap Diagnosis

1. **New Knowledge (theoretical):** The Bayesian formalization (Lemma 1) and the closed-form result (Lemma 2) constitute genuine new theoretical knowledge. However, the practical significance of Lemma 2 is weakened by its restrictive assumptions, which are not cleanly verified in real-world settings.

2. **Reproducibility/Reusability:** The LSE algorithm is simple and reusable. The code is available on GitHub. However, the lack of sample-size guidance and the log-bias issue reduce immediate reusability.

3. **Impact on Practice/Understanding:** The paper's main practical impact is the insight that when Assumption 3 fails (as it does for the dot product critic), the LSE method provides a principled fallback. This is a useful practical message, but it is currently buried in the experimental analysis rather than highlighted as a central takeaway.

### Proposed Research Experiments

#### Experiment P0.1 — RL Direct+Average ablation (P0 priority)
- **Target Claim:** LSE's marginalization is responsible for its 20-30% RL improvement
- **Hypothesis:** A "Direct+Average" baseline (max_a 1/N Σ_i ϕA(s,a)⊤ϕB(sf_i) compared to ϕC(ℓ)) will perform worse than LSE but better than Direct, confirming both distributional information and composition matter
- **Minimal Design:** Use the same sf samples for both LSE and Direct+Average; same encoder checkpoints
- **Controls/Baselines:** Direct (no sf), Direct+Average (with sf, no composition), LSE (full)
- **Metrics:** Success rate, average steps to goal
- **Success Criterion:** LSE outperforms Direct+Average by >5%, establishing composition's unique contribution
- **Estimated Cost/Time:** 1-2 GPU hours (reuse existing encoders)
- **Expected Paper-Quality Gain:** High — resolves the primary confound in the RL experiment

#### Experiment P0.2 — Non-linear synthetic variant (P1 priority)
- **Target Claim:** The "Law" holds under non-Gaussian, non-linear data generation
- **Hypothesis:** Performance degrades gracefully as non-linearity increases
- **Minimal Design:** Generate B from a mixture of Gaussians or via a shallow neural network from a latent variable; generate A and C via nonlinear projections (MLPs)
- **Controls/Baselines:** Linear Gaussian baseline (same as current), LSE method
- **Metrics:** Recall@1 at different non-linearity levels
- **Success Criterion:** Report recall degradation curve; if recall drops below 80% of linear baseline, identify the violation mode
- **Estimated Cost/Time:** 3-5 GPU hours
- **Expected Paper-Quality Gain:** Medium — strengthens robustness claims and sets realistic expectations

#### Experiment P0.3 — Broader uniformity test (P1 priority)
- **Target Claim:** Assumption 3 (uniform marginals) holds for real-world representations
- **Hypothesis:** CLIP/CLAP language representations are *not* uniformly distributed when tested on a broader, more natural corpus
- **Minimal Design:** Use a diverse corpus (e.g., 10K Wikipedia captions or MS-COCO captions) instead of the AudioSet ontology; compute KS test or alternative uniformity metric (e.g., mean cosine similarity)
- **Controls/Baselines:** AudioSet ontology test for comparison
- **Metrics:** KS p-value, mean pairwise cosine similarity
- **Success Criterion:** Report whether uniformity is rejected on the broader corpus; if so, provide practical guidance
- **Estimated Cost/Time:** 1 GPU hour
- **Expected Paper-Quality Gain:** Medium — provides honest empirical grounding for Assumption 3

### ASCII Diagram — Experiment Upgrade Plan

```text
Current experiments:
Linear Gaussian synthetic (E1)     -> Self-fulfilling verification
CLIP/CLAP on AudioSet (E3)        -> No sample-size guidance
RL navigation (E6)                 -> Confounded comparison

Proposed additions (P0 prioritized):
[P0.1: RL Direct+Average ablation]
    -> P0.1 isolates marginalization vs information benefit
    -> Expected: clarifies the source of LSE's advantage

[P0.2: Non-linear synthetic variant]
    -> Tests robustness beyond linear Gaussian
    -> Expected: quantifies assumption violation tolerance

[P0.3: Broader uniformity test]
    -> Tests Assumption 3 on diverse language corpus
    -> Expected: honest assessment of when A3 holds

[P1.1: Decision rule in conclusion]
    -> Synthesizes all findings into practical guidance

Readiness for resubmission after P0.1-P0.3 + P0.1-P0.6 text edits:
- Theoretical claims: properly bounded and qualified
- LSE method: actionable with guidance
- RL results: causally interpretable
- Assumption 3: empirically grounded
```

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score: 6.5 / 10**

**Rationale:** The paper addresses a timely and important question with an elegant theoretical framing. The connection between contrastive representations and Bayesian marginalization (Lemma 1) is a genuine conceptual contribution, and the LSE algorithm has practical value. However, the score is reduced by the following factors:

- **Research value (primary dimension):** The core theoretical result (Lemma 2, the "Law") is narrower than initially presented because it depends on restrictive assumptions that are frequently violated. The more robust contribution (Lemma 1 + LSE) receives less emphasis, reducing the paper's actionable impact. **Score contribution: 6/10**
- **Novelty (primary dimension):** The Bayesian formalization is novel, but the experimental validation is partially circular (LanguageBind) or self-fulfilling (synthetic data). The paper would benefit from a clearer separation of what is new vs. what is formalized from prior geometric/probabilistic insights. **Score contribution: 6/10**
- **Validity/Soundness:** The theoretical derivations appear sound aside from a typographical error in Lemma 2's proof. The experiments are generally well-designed but have confounds (RL) and over-claims (LanguageBind validation). **Score contribution: 7/10**
- **Reproducibility:** The LSE algorithm is simple and code is provided. The main text lacks sample-size guidance. **Score contribution: 6/10**
- **Presentation:** The writing is clear but the narrative structure could better separate the two contributions and their assumption requirements. **Score contribution: 7/10**

**Post-Revision Target: [7.5, 8.5] / 10**

If the authors address all P0 items (particularly bounding claims, adding LSE guidance, clarifying LanguageBind validation, and addressing the compatible-intermediate-space issue) and at least two P1 items (RL ablation, expanded conclusion), the paper could reach 7.5-8.5. The upper bound assumes addition of the non-linear synthetic variant and broader uniformity test, which would strengthen the empirical grounding. The paper is already accepted at ICLR 2025, so these revisions would strengthen the archival version for broader impact.