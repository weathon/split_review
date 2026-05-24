## Summary

This paper introduces LAFT (Language-Assisted Feature Transformation), a training-free method that uses CLIP's shared embedding space to construct concept subspaces from pairwise differences of text features. By projecting image features onto (guide) or orthogonal to (ignore) these subspaces, users can selectively emphasize or suppress specific visual attributes using natural language prompts. The method is combined with a kNN classifier for semantic anomaly detection (LAFT AD) and integrated with WinCLIP for industrial anomaly detection (WinCLIP+LAFT). Experiments on Colored MNIST, Waterbirds, CelebA, MVTec AD, and VisA demonstrate strong performance, particularly on semantic AD tasks where LAFT AD significantly outperforms CLIP-based baselines.

## Strengths

1. **Training-free and broadly applicable**: LAFT requires no additional training or fine-tuning of CLIP — it only uses the pre-trained text and image encoders (Section 4). This is a genuine differentiator from methods like InCTRL and adapter-based approaches that need dataset-specific pre-training. The method is demonstrated across both semantic AD (Tables 1–2) and industrial AD (Table 3) without redesign.

2. **Both guide and ignore operations via language alone**: Section 4.3 defines two complementary projections: $T_{\text{guide}}$ (onto the concept subspace) and $T_{\text{ignore}}$ (orthogonal to the nuisance subspace). Prior work like Red PANDA requires labeled nuisance-attribute data. LAFT achieves both operations using only text prompts, which is a meaningful step forward in controllability.

3. **Robustness to incomplete attribute knowledge**: The ablation on prompt quality (Table 4) is the paper's strongest empirical contribution. It systematically varies concept values (seen normal, unseen anomaly, auxiliary) and shows that performance degrades gracefully when only partial knowledge is available. For example, guiding with only seen normal values on Colored MNIST still achieves 96.2 AUROC vs. 98.5 with full knowledge — a practically important result.

4. **Clean, well-motivated idea**: The method is simple to describe and implement. Using arithmetic operations on text embeddings (inspired by Mikolov 2013) + PCA to construct concept axes is intuitive and clearly connected to the problem of attribute-specific anomaly detection. Figure 3 visualizes the effect convincingly.

## Weaknesses

### Major

None. The core claims are supported by the experiments, and no single issue threatens the validity of the contributions.

### Minor

1. **The "concept subspace" construction lacks a characterization of when it will/will not work.** The paper asserts that projecting onto the concept subspace "retains only the relevant attributes of the image feature, as irrelevant attributes are nearly orthogonal to the concept axes" (Section 4.3), but provides no evidence for this orthogonality claim beyond a 2D visualization (Figure 3). The approach works on the tested datasets, but the paper does not analyze what fraction of irrelevant variance remains, whether there are attributes for which CLIP's embedding does not support linear separability, or what happens when the target attribute is correlated with nuisance attributes in the embedding space. This limits confidence in transferring to settings with fine-grained or abstract attributes. The paper is transparent that this is a hypothesis ("We hypothesize that visual concept subspaces exist," Section 1), but the discussion section does not address potential failure modes.

2. **The formal information-theoretic framework (Equations 1–2) is introduced but never operationalized.** The paper defines invariance via conditional independence and informativeness via mutual information, then says "Empirical evaluations of these measures... are provided in the Experiments." However, the experiments only report AUROC — they do not measure mutual information, conditional independence, or directly test whether irrelevant attributes are actually suppressed in the transformed features. The formal framework serves as motivation but is not validated or measured. This is a disconnect between the mathematical framing and the empirical evidence.

3. **No sensitivity analysis on the key hyperparameter $d$ (number of PCA components) in the main paper.** The paper states that $d$ is selected "between 8 and 32 when guiding an attribute, and between 32 and 384 when ignoring" (Section 4.2), and refers to the ablation study — but the ablation study in the main paper (Table 4) focuses on prompt quality, not $d$. The appendix is stripped, so readers cannot assess how sensitive the method is to this hyperparameter. Since $d$ is the only tunable parameter of the method itself, this is a transparency issue.

4. **Industrial AD gains are modest.** On MVTec AD and VisA (Table 3), WinCLIP+LAFT-C improves over WinCLIP+ by 0.2–2.2% AUROC across settings, with several improvements under 1% and many within one standard deviation. The paper honestly calls this a "proof of concept" (Section 5.2), and it does not detract from the semantic AD story, but the significance of the industrial AD contribution is limited.

5. **Baseline prompts for the CelebA eyeglasses task appear poorly chosen.** MCM achieves only 5.7 AUROC and CLIPN-C achieves 1.4 AUROC on the Eyeglasses attribute (Table 2), while LAFT AD achieves 98.1. Such extreme scores suggest the baseline prompts may not be well-suited for this attribute. The paper should clarify what prompts were given to those baselines, because as presented the comparison looks weaker than it could be.

### Trivial

- The paper uses cosine similarity and $k=30$ for kNN without justification (Section 4.4). Cosine similarity is natural for CLIP's normalized embeddings and $k=30$ is standard, but a brief justification would be helpful.

## Nice-to-Haves

- A discussion of failure cases: when would LAFT not work? (e.g., attributes not linearly separable in CLIP's space, highly correlated target and nuisance attributes, attributes that cannot be described with text prompts)
- Measuring what is retained/suppressed by the projection directly (e.g., predicting bird type vs. background from projected features on Waterbirds) rather than only through downstream AD performance
- A sensitivity plot of performance vs. $d$ for at least two datasets in the main paper

## Removed Points

These points were flagged by reviewers but removed after verification:

- **"O(n²) pairwise differences not justified"** — The paper explicitly motivates this via Mikolov (2013)'s finding that text embedding differences capture semantic relationships. This is a design choice, not a weakness.
- **"kNN baseline without std"** — The paper states "Standard deviations are computed over five different seeds, with results for deterministic cases omitted." This explains the omission.
- **"Comparisons not fully controlled because task definition favors LAFT"** — The paper acknowledges this (Section 5, paragraphs 1–2), clearly separates baseline/guide/ignore groups in tables, and provides the fairest comparison (kNN on the same subset). The framing is appropriate given the paper's stated goal.
- **"Missing failure cases discussion"** — Moved to Nice-to-Haves; it is a suggestion for improvement, not a weakness of the presented work.

## Novel Insights

The reviews surface one observation worth highlighting: the paper's core contribution — using pairwise differences of text embeddings to construct a concept subspace — is conceptually related to techniques for interpreting CLIP's internal representations (e.g., the TextBase decomposition in the ICLR 2024 oral "Interpreting CLIP's Image Representation via Text-Based Decomposition"). That paper shows that CLIP's attention heads encode property-specific directions (shape, color, etc.) and that removing certain heads can suppress spurious features. LAFT's approach of using text-difference vectors + PCA is a simpler, task-agnostic way to achieve a similar effect without analyzing individual heads. This connection, not discussed in the paper, provides a potential explanation for why the concept subspace approach works: CLIP's embedding space may already contain approximately linear attribute directions that difference vectors can extract.

## Suggestions

- Add a sensitivity analysis on $d$ (number of PCA components) to the main paper, with a plot or table for at least two datasets. This is the only tunable hyperparameter and the community needs to understand its impact.
- Discuss potential failure modes explicitly: when might the orthogonality assumption fail? What types of attributes are not linearly separable in CLIP's space? A limitations paragraph would significantly strengthen the paper.
- Clarify what prompts were given to MCM and CLIPN baselines on the CelebA eyeglasses task, and explain why their performance is near chance. If those prompts are suboptimal, note this and provide a more informative comparison.

## Score and Decision

### Calibration

**Round 1 (bracketing):**
- Weak anchor band: papers scoring 2.20–3.00 (rejected/withdrawn) — e.g., "CLAD" (2.20), "Is Scale All You Need" (3.67) \[clearly weaker than LAFT\]
- Middle anchor band: papers scoring 3.67–6.75 — e.g., AnomalyCLIP (6.17, poster), One-for-All (6.40, poster), "Rotation Has Two Sides" (5.40, spotlight) \[comparable range\]
- Strong anchor band: papers scoring 8.00+ (oral/spotlight) — e.g., "Interpreting CLIP's Image Representation" (8.00, oral) \[clearly stronger\]

**Round 1 bracket:** 5.0 – 7.0

**Round 2 (narrowing within bracket):**
- Compared against AnomalyCLIP (avg 6.17, poster): AnomalyCLIP evaluates on 17 datasets but requires prompt tuning (training cost, additional parameters). LAFT is training-free and has a cleaner idea but fewer datasets. Comparable quality; LAFT slightly cleaner contribution.
- Compared against One-for-All (avg 6.40, poster): Introduces a new task paradigm with more comprehensive few-shot industrial evaluation. LAFT has simpler idea and training-free advantage but less extensive experiments. Modestly below.
- Compared against Hard-to-Beat Baseline (avg 6.00, poster): Training-free CLIP adaptation for classification. Similar simplicity/training-free philosophy, but anomaly detection is harder than classification. Comparable.
- Compared against Rotation Has Two Sides (avg 5.40, spotlight): More extensive analysis but narrower scope (rotation-specific). LAFT has broader applicability. LAFT is stronger.

**Final position:** The paper is comparable to accepted poster-level CLIP anomaly detection papers (AnomalyCLIP, One-for-All), with the advantages of being training-free and having a cleaner idea, balanced against less comprehensive evaluation. It is clearly above rejected/weak papers in this space.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>