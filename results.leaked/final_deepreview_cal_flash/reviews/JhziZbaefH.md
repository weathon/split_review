## Summary

This paper studies online multimodal learning (OML), where a model continuously learns new multimodal concepts and associations without forgetting. The authors propose a brain-inspired hierarchical neural architecture with ascending, descending, and lateral pathways, featuring a reference extraction algorithm (based on coefficient of variation) that autonomously identifies which features a word refers to, and a conflict detection mechanism that asks the user questions when inputs contradict prior knowledge. The method is evaluated on small custom datasets of images of fruits/home objects paired with spoken Chinese names and compared against both offline multimodal methods and online learning baselines.

## Strengths

1. **Novel reference extraction mechanism.** The coefficient-of-variance-based algorithm (Section 3.4) that autonomously identifies which feature dimensions a word refers to is clever and well-motivated. In the precise-referring experiment (Table 2), OML is shown to distinguish between name words (which refer to all object features) and color words (which refer only to color features), a capability absent in prior online methods ART and AEN. This is a genuine technical contribution.

2. **Demonstrated online continual learning without catastrophic forgetting.** In the open-environment experiments (Table 1), OML maintains stable accuracy across sequential data chunks while offline methods (DAE, DBM, DJSRH, NRCH, FUME) drop significantly due to catastrophic forgetting (e.g., Fruits Open V→A: OML 89.8% vs. next-best online AEN 86.2% vs. offline DAE 52.3%). The ability to add new modalities post-training (Table 3, taste modality added after vision+audition) is also demonstrated and outperforms AEN on all cross-modal retrieval tasks.

3. **Conflict detection with human-in-the-loop interaction.** The paper implements a rule-based conflict detection system (Section 3.5, Cases 1–4) that checks for consistency between visual and auditory inputs and asks appropriate questions when mismatches are detected. While the interaction mechanism is simple (deterministic templates), the paper reports 100% conflict detection in a controlled test with 10% mispaired inputs (Section 4.1(3)), demonstrating the architecture's ability to flag inconsistencies.

4. **Modular, growing architecture for online learning.** The design of separate feature neurons, unimodal association neurons (with order-dependent and order-independent modes), and multimodal association neurons provides a principled way to grow the network as new concepts arrive, with clear mechanisms for when to add new neurons and connections.

## Weaknesses

### Major

1. **Unfair comparison framing against offline methods in Table 2.** The precise-referring experiment evaluates offline methods (DAE, DBM, DJSRH, NRCH, FUME) that were trained on the base dataset and *frozen*, then tested on the enhanced dataset (E-Fruits/E-HomeF) that includes entirely new color words. The accuracy drops marked ↓ and the claim that OML "gets the highest accuracy" in this setup is a foregone conclusion — fixed models cannot learn concepts they were never trained on. This comparison demonstrates only that frozen models fail on unseen classes, not that OML's specific mechanisms are better. A proper comparison would retrain offline methods from scratch on the full E-dataset, or at minimum contextualize these results as a test of *adaptability* rather than *accuracy*. The comparison against *online* methods (ART, AEN) in the same tables is valid and informative, but the framing against offline methods is misleading.

2. **No ablation studies.** The architecture has multiple interacting components: Fourier-domain signaling in feature neurons, the coefficient-of-variance reference extraction, the descending pathway conflict mechanism, lateral connections, the λ-based pathway matching for modal extension. Not a single component is ablated. It is impossible to determine which parts drive the reported results. The Fourier transform mechanism (Eq. 1–6) is particularly undersupported — the paper never compares against simpler gating or distance-based matching mechanisms, so the complexity is not justified.

3. **No statistical rigor.** Every reported result in Tables 1–3 is a single point estimate with no error bars, confidence intervals, or replication across random seeds. Given the small dataset sizes (custom-curated Fruits and HomeF), this is a serious omission. The claim of "100% conflict detection" is reported as a single sentence with no experimental protocol, trial count, or false-positive analysis.

4. **Narrow evaluation scope relative to claims.** The paper claims to address "online multimodal learning" as a general problem but evaluates exclusively on small, author-curated datasets of fruit and home-object images with Chinese spoken names (following Xing et al. 2019/2021). Features are hand-crafted (Fourier descriptors for shape, MFCCs for speech, SAM for segmentation). No evaluation is conducted on any standard continual learning benchmark (e.g., Split CIFAR, 5-Datasets, CORe50) or standard multimodal retrieval benchmark (e.g., Flickr30K, MS-COCO). The abstract's claim that the method "can effectively handle the online multimodal learning" is unsupported at this scale.

### Minor

5. **Oversold interaction capability.** The introduction's "garnet vs. red" dialogue (Figure 1) implies semantic reasoning about lexical relationships ("You also call it garnet?"), but the actual implementation (Section 3.5) consists of four deterministic conditional branches with hardcoded question templates and binary yes/no answers. The paper is transparent about the mechanism in the method section, but the framing in the introduction creates expectations the system does not meet. The system does not parse natural language feedback, handle ambiguous responses, or demonstrate generalizable interactive reasoning.

6. **Limited online method comparison.** Only two other online methods are compared (ART and AEN). For the modal extension experiment (Table 3), only AEN is compared. Given that the paper argues against catastrophic forgetting, standard continual learning methods (e.g., EWC, SI, MAS, experience replay) could be adapted to this multimodal setting at least as baselines. The paper does not discuss how such methods might apply or why they are unsuitable.

### Trivial

7. **Naming inconsistency.** In the experimental setup, the system is referred to as "OLM" (line 244: "if the question posed to the user by OLM remains unanswered") rather than "OML."

## Nice-to-Haves

- **Complexity and memory analysis.** The paper describes a growing network architecture but never reports how many neurons are added, how the network scales with concepts, or the computational/memory costs of the Fourier-domain signaling.
- **Analysis of reference extraction failure modes.** The paper does not characterize cases where the coefficient-of-variation heuristic might fail (e.g., when all features are equally stable/unstable, or when the "referring" feature is dimensionally unstable).
- **Ablation of the Fourier transform mechanism.** Replacing the Fourier-domain signaling with simpler distance-based matching would help justify the architectural complexity.

## Removed Points

These points were flagged by reviewers but are removed or demoted after verification against the paper:

- **"Scoring rule in Table 2 is inconsistent"** — The harsh critic claimed the metric is tailored to favor OML because AEN retrieving *all* features is counted as correct. However, the paper explicitly states this is the case ("we count this as a correct result for them in Table 2"), which is a transparent and *generous* treatment of the baseline, not a manipulation. **Removed:** factually incorrect criticism.
- **"The evaluation is staged to guarantee OML appears to win (Structural)"** — This was characterized as a fatal/structural flaw. While the comparison against offline methods in Table 2 is indeed problematic (retained as Major weakness #1), the paper also provides fair comparisons: Table 1 against online methods ART/AEN, Table 3 against AEN, and the close-environment results where offline methods perform well. The critic's framing of this as a fatal flaw that "invalidates the central claim" overstates the case. **Demoted** from Fatal to Major and rephrased.
- **"Pure formatting/style nitpicks"** — Not present in the inputs.
- **"Missing related works"** — The critic suggests comparing to EWC, SI, MAS, experience replay. This is a valid suggestion (retained as Minor weakness #6), but the instruction prohibits me from generating missing related works on my own authority. The critic's suggestion is kept only because it came from the reviewer, not from my own knowledge.
- **"Missing appendix/proofs"** — The critic's "Missing Parts" section alludes to parts that may exist in a stripped appendix. Removed per instructions.
- **"The method is not a general interactive learning system"** as a fatal weakness — The paper describes the interaction mechanism accurately in Section 3.5. The gap is between the introduction's framing and the implementation, which is retained as Minor weakness #5, not a fatal flaw.

## Novel Insights

None beyond the paper's own contributions. The reviewer inputs do not offer a novel synthesis that the paper itself does not already contain.

## Suggestions

1. **Add ablation studies** for the key components: Fourier-domain signaling, reference extraction, conflict detection, and lateral connections. A minimal starting point is comparing OML against versions with (a) the Fourier mechanism replaced by simple distance-based matching and (b) the reference extraction replaced by a naive baseline (e.g., always selecting the first feature type).

2. **Fix the Table 2 comparison** by also reporting results where offline methods are retrained from scratch on the full E-dataset. Frame the comparison against frozen baselines as a test of *adaptability* rather than making it an "OML wins on accuracy" claim.

3. **Report error bars** across at least 3--5 random seeds or data orderings. This is essential for any experimental paper, especially one with small datasets.

4. **Broaden the evaluation** to at least one standard continual learning benchmark (e.g., an incremental version of CIFAR-100 with text descriptions) and/or one standard multimodal retrieval benchmark, even if the method requires modification. Alternatively, reframe the paper's scope more modestly to match the evaluation.

5. **Tone down the human-interaction claims** to match what is actually implemented: rule-based yes/no templates, not general semantic dialogue. The "garnet" example in the introduction should be explicitly qualified as an illustration of the intended use case, not a description of the implemented capability.

## Score and Decision

**Round-1 (Bracketing) anchors — three bands:**

| Anchor | Avg Score | Round | Comparison to this paper |
|--------|-----------|-------|------------------------|
| gNoqEdT2wO (multimodal CL benchmark) | 2.33 | R1 | Much weaker — pure benchmark without new method; paper has more contribution |
| Pa6SiS66p0 (beyond unimodal learning) | 4.33 | R1, R2 | Similar — has a CL benchmark but weak baselines; our paper has more methodological novelty |
| BZWssJoYEv (multimodal interaction info-theoretic) | 5.50 | R1 | Similar evaluation scope concerns but stronger theory; our paper is architecturally richer |
| TPZRq4FALB (test-time adaptation) | 8.00 | R1 | Much stronger — clean problem framing, standard benchmarks, rigorous evaluation |

**Initial bracket (Round 1):** 3.5 – 6.0

**Round 2 (Narrowing) anchors:**

| Anchor | Avg Score | Round | Comparison to this paper |
|--------|-----------|-------|------------------------|
| CagdoUkvvl (relaxing representation alignment) | 4.50 | R2 | Similar — multimodal CL method with missing ablations and limited novelty claims; our paper has more novel components but narrower evaluation |
| G9Ea7mlqGO (CLIP online continual learner) | 3.80 | R2 | Weaker — limited contribution, some flawed reasoning; our paper has clearer contributions |
| BrqFB8Nl7e (continual learning after deployment) | 3.75 | R2 | Weaker — mostly problem setting with limited method; our paper has more architectural substance |
| UhKkWHkvfg (analytic continual TTA) | 5.00 | R2 | Comparable — method contribution with evaluation gaps; our paper has similar strength but different weaknesses |
| 86zAUE80pP (CPPO) | 6.25 | R2 | Stronger — accepted paper with clearer problem, more standard evaluation, and manageable weaknesses |

The paper sits between the 4.33–5.00 rejected anchors and the 6.25 accepted anchor. Like the 4.33–5.00 papers, it has genuine methodological novelty but suffers from significant evaluation gaps (no ablations, no error bars, narrow scope, partially misleading comparisons). Unlike the 6.25 CPPO paper, which had standard evaluation and clearer motivation despite some missing analyses, this paper's evaluation package is substantially weaker.

**Final score: 4.5**

A score of 4.5 reflects that the paper has a genuinely novel approach (reference extraction, conflict-aware growing architecture) to an interesting and underexplored problem, but the evaluation is too limited in scope, rigor, and fairness to support the broad claims. The paper could become publishable with major revisions focused on ablation studies, statistical rigor, broader benchmarking, and more honest comparison framing.

**Decision: Reject**

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>