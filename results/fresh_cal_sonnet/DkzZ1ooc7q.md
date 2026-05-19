Now let me run the Round 1 calibration search to bracket this paper's score.Let me read two more relevant anchors in detail:Now I have enough information to write the final consolidated review. Let me compile it.

---

## Summary

OmniSep proposes the first unified sound separation framework that handles text, image, and audio queries within a single model. The key technical contribution is **Query-Mixup** (Eq. 1), a training strategy that blends query features from different modalities with randomly sampled weights, allowing simultaneous optimization across all modalities. Two inference-time extensions are introduced: a **negative query** formulation (Eq. 4, Q' = (1+α)Q − αQ_N) that suppresses unwanted sounds, and **Query-Aug**, a retrieval-augmented approach for handling unrestricted natural-language descriptions. Evaluations on MUSIC, VGGSOUND-CLEAN+, and MUSIC-CLEAN+ datasets report state-of-the-art SDR across TQSS, IQSS, and AQSS tasks.

---

## Strengths

1. **First unified framework across all three query modalities with composed-query support.** No prior work handles text, image, and audio queries in a single model or enables composed multi-modal queries for sound separation. This is a concrete, first-of-its-kind contribution.

2. **Consistent state-of-the-art performance across all tasks and datasets.** Table 1 shows OmniSep surpasses the strongest per-task baselines on every dataset: e.g., MUSIC TQSS Mean SDR of 10.65 vs. AudioSEP's 9.82; VGGSOUND-CLEAN+ AQSS of 7.12 vs. the prior AQSS [lee2019audio]'s 5.34. The improvements are not marginal.

3. **Ablation (Table 2) directly supports Query-Mixup's value within the same backbone setup.** Table 2 rows #4→#5 show Query-Mixup raises AVG SDR from 6.45 to 6.70 (VGGSOUND-CLEAN+), and crucially recovers the TQSS performance of a text-only trained model (#1: 6.70) while maintaining strong IQSS (#5: 6.69 vs. #4: 6.53). This directly substantiates the "unified training without cross-modal degradation" claim.

4. **Negative query is robust to the choice of α.** Figure 1 demonstrates that the proportional-weighting method (Eq. 4) yields Mean SDR variation ≤ 0.45 across α ∈ [0, 2] on both datasets and all query types, while naive subtraction collapses to 4.32 on VGGSOUND-CLEAN+ TQSS at α=2. The robustness advantage is cleanly demonstrated.

5. **UMAP visualization provides interpretable mechanism for Query-Mixup.** Figure 2 shows that ImageBind embeddings from different modalities form distinct clusters, motivating the gap-bridging role of mixed embeddings and grounding the compositional query capability.

---

## Weaknesses

### Fatal
None.

### Major

- **The main comparison in Table 1 conflates the ImageBind backbone upgrade with the Query-Mixup contribution.** CLIPSEP uses CLIP as its query encoder; OmniSep uses ImageBind — a substantially stronger multi-modal encoder that explicitly aligns text, image, and audio into a shared space. The headline TQSS improvement over CLIPSEP-Text (7.91→10.65 on MUSIC, 5.49→6.70 on VGGSOUND-CLEAN+) could be explained in part by this backbone upgrade. The paper never reports the one informative control — CLIPSEP architecture with ImageBind as the encoder and *without* Query-Mixup. This baseline is needed to isolate what Query-Mixup contributes to Table 1's numbers vs. the backbone switch. Table 2 does provide within-backbone evidence (Query-Mixup adds +0.25 AVG SDR in row #4→#5), but the cumulative gain attributed to the full system vs. CLIPSEP-era baselines remains undecomposed. This directly limits confidence in the headline "state-of-the-art" claim.

- **Query-Aug is framed as "open-vocabulary" but tests only surface-form robustness.** Section 4.4 and Table 3 use GPT-3.5 to rewrite class labels already in the dataset into alternative phrasings (e.g., "dog barking" → "A dog letting out barking noises"; "tapping guitar" → "Tapping on a guitar to produce rhythms"). These paraphrases are semantically nearly identical to the original labels and preserve the same in-domain concept. Nearest-neighbor retrieval in Query-Aug trivially maps back to the correct in-domain label in virtually every case, which explains why Experiment #11 (6.32 SDR) nearly recovers in-domain performance (#7: 6.70). This does *not* demonstrate generalization to sound concepts not present in the training vocabulary. A genuine open-vocabulary test would require descriptions of sounds absent from VGGSound's 330 categories.

### Minor

- **Negative query evaluation relies on implicit oracle access to the interfering signal.** Applying Q_N requires semantic knowledge of which sound is interfering at inference time. In Table 1, this is implicitly provided by the evaluation setup (ground-truth pairs). For a real-world deployment scenario, a user would need to separately identify the unwanted sound class before applying NQ. The paper notes "negative query information" in passing but does not characterize how sensitive performance is to imperfect or noisy Q_N, nor describe a realistic deployment pipeline. Given that NQ improvements form a substantial portion of the reported gains (+0.87 Mean SDR on VGGSOUND-CLEAN+ TQSS), this deserves at least a brief discussion.

- **The weight sampling distribution for Query-Mixup is unspecified.** Equation 1 states w_a, w_v, w_t ∈ [0, 1] but neither the methods section nor the implementation appendix (Section A) specifies how these weights are sampled during training (uniform, Dirichlet, sparse with dropout probability, etc.). This materially affects what the model sees during training and is essential for reproducibility.

- **Composed omni-modal query gain is small on MUSIC (11.03 vs. 10.97 IQSS).** The motivation for composed queries — that cross-modal information is complementary — predicts larger gains when all modalities are combined. On MUSIC, the gain is only 0.06 SDR. VGGSOUND-CLEAN+ shows a more meaningful gain (7.46 composed vs. 7.12 AQSS best), but the MUSIC result weakens the complementarity argument.

### Trivial

- The ablation (Table 2) is run only on VGGSOUND-CLEAN+; a brief check on MUSIC for the key rows (#4 and #5) would confirm whether trends generalize across domains.

---

## Nice-to-Haves

- Adding the missing control baseline (CLIPSEP architecture + ImageBind, no Query-Mixup) would directly quantify how much the backbone vs. the method contributes and would substantially strengthen the paper's main claim.
- Including at least a few examples from genuinely out-of-domain sound categories in the Query-Aug evaluation (e.g., sounds not in VGGSound's 330 classes, accessed via descriptive text) would substantiate the "open vocabulary" claim rather than surface-form robustness.
- A brief analysis of NQ sensitivity to imperfect negative queries (e.g., slightly mismatched sound category as Q_N) would characterize the practical robustness of this inference-time extension.
- The introduction motivation — that OmniSep enables scaling audio data by separating wild mixtures — is stated but never validated experimentally. Even a brief discussion or pointing to future work would close this gap.

---

## Removed Points

*These points are flagged to be removed, treat them with caution.*

- **[Harsh Critic] "The scaling motivation is dropped entirely"** — Removed from Weaknesses. This is a framing observation; the paper's core claims are about sound separation performance, not downstream dataset scaling. The motivation is in scope even without a data-scaling experiment.

- **[Harsh Critic] "AQSS baseline is solely from 2019"** — Demoted to removed. Per the hard rules, the paper cannot be criticized if no competitive AQSS baseline exists in the literature; the harsh critic even acknowledges this. The fact that "OmniSep's AQSS gains are massive but uninformative given the weak baseline" is a soft concern but not a real weakness if the authors genuinely state there are no stronger recent AQSS-specific methods.

- **[Harsh Critic] "Table 1 asterisk reproduction quality not validated"** — Removed. Speculative concern without evidence that the reproduction is wrong.

- **[Harsh Critic] "Negative query mechanistic explanation should be more precise"** — Removed as Trivial/presentation. The algebraic behavior of Eq. 4 is clear and the empirical advantage is well-demonstrated in Figure 1.

- **[Strength Finder] "Query-Aug enables open-vocabulary separation comparable to in-domain"** — Removed as stated. While numerically true (#11: 6.32 > #6: 5.49), this comparison mixes backbone upgrades with the Query-Aug effect. It cannot be treated as a clean strength given the Major weakness about confounded comparison.

- **[Strength Finder] "Qualitative results confirm separation quality"** — Removed as generic. The spectrogram visualizations are useful but constitute standard qualitative presentation, not a distinct strength.

---

## Novel Insights

The Query-Mixup strategy is an elegant solution to a concrete and underappreciated problem: when training a model on multiple query modalities by alternating between them (as CLIPSEP does), the training objective is inherently unstable and single-modal performance degrades. Query-Mixup sidesteps this by fusing the query embeddings during training, forcing the separation network to operate in the convex hull of the embedding space, which then naturally enables composed multi-modal queries at inference. This insight — that *training on mixtures* enables *inference with compositions* — is the paper's most transferable idea and extends naturally to other multi-modal conditional generation tasks where the same instability appears.

---

## Suggestions

1. Add the single missing control: train CLIPSEP's architecture on the same data with ImageBind as the frozen encoder, **without** Query-Mixup. Include this in Table 2 or as a footnote to Table 1. This is a one-experiment fix that resolves the major confound.
2. Replace or augment the Query-Aug evaluation with a condition that uses descriptions of sounds genuinely absent from VGGSound (e.g., write 10–15 hand-crafted descriptions of exotic or compositional sounds and test retrieval + separation). Even a qualitative analysis would support the open-vocabulary framing.
3. Specify the weight sampling distribution in Eq. 1 (e.g., "we sample each weight independently from Uniform[0,1]" or "we use a sparse sampling scheme where one weight is 1 and others are 0 with probability p"). This is a one-sentence fix.

---

## Score Calibration

**Round 1 bracket (3 bands):**

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| Weakly-supervised Audio Separation (4N97bz1sP6) | 6.67 | 1 | Topically closest; more technically novel (no single-source data at train time), but similar scope |
| Separate and Diffuse (UXALv0lJZS) | 6.00 | 1 | Similar SDR framing, cleaner theory, narrower scope |
| OmniBind (l2izo0z7gu) | 6.25 | 2 | Multi-modal binding, broader scope, similar confounded-comparison weakness |
| Typing to Listen (pyuCmLLluu) | 5.50 | 2 | Rejected; similar modality-extension framing for audio extraction, narrower scope |
| DM-Codec (UFwefiypla) | 3.00 | 1 | Weaker, rejected speech tokenization; clearly below OmniSep |
| Test-time Adaptation READ (TPZRq4FALB) | 8.00 | 1 | Much stronger theoretical and empirical rigor; out of reach |

**Round 1 bracket: 5.0–7.0**

**Round 2 narrowing:** The most topically relevant anchors in this range are:
- **Weakly-supervised Audio Sep (6.67, Accept)**: More methodologically rigorous (novel training paradigm, clean baselines, no backbone confound), but OmniSep covers more tasks. OmniSep is weaker on methodological completeness — the critical isolation ablation is missing, and the open-vocabulary claim is overstated.
- **Separate and Diffuse (6.0, Accept)**: Comparable scope and empirical rigor. OmniSep is broader (three tasks vs. one) but has a larger methodological gap.
- **OmniBind (6.25, Accept)**: Similar multi-modal unification spirit, similar "confounded by prior models" concern. OmniSep's scope is narrower (separation only) but more focused.
- **Typing to Listen (5.5, Reject)**: Rejected; OmniSep is clearly stronger — more datasets, multiple tasks, concrete Query-Mixup ablation, and more comprehensive baselines.

OmniSep is **above** "Typing to Listen" (5.5) clearly, and **below or comparable to** "Weakly-supervised Audio Sep" (6.67). Its proximity to "Separate and Diffuse" (6.0) and "OmniBind" (6.25) is close. The missing backbone isolation ablation is the deciding factor: it prevents the headline contribution from being cleanly established, which is the distinguishing weakness from the 6.25–6.67 papers. I place the paper at **5.5**, slightly below the 6.0 anchor, because the confound concern is substantive enough to push below the "Separate and Diffuse" threshold.

---

**Originality:** Moderate-high. The unified omni-modal framing and Query-Mixup strategy are novel, though the architecture largely follows CLIPSEP with a backbone swap and training modification.

**Importance of research question:** High. Sound separation is a genuine bottleneck for audio data scaling; multi-modal queries are practically motivated.

**Support for claims:** Moderate. Within-backbone ablation (Table 2) is convincing for Query-Mixup; headline comparison vs. CLIPSEP is confounded by the backbone switch.

**Soundness of experiments:** Moderate. Three datasets, consistent improvements, reasonable baselines, but missing key isolation experiment and oracle assumption in NQ.

**Clarity of writing:** Good. The paper is well-organized and readable.

**Value to research community:** Moderate-high. First unified model across text/image/audio query types; publicly released code and demo page.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>