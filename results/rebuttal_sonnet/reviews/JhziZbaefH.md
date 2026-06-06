## Summary

The paper proposes OML, a brain-inspired hierarchical online multimodal learning network combining feature neurons (FN), unimodal association neurons (UAN), and multimodal association neurons (MAN) connected via ascending, descending, and lateral pathways. Key contributions include: (1) online growing architecture that avoids catastrophic forgetting; (2) a coefficient-of-variation-based reference extraction algorithm that binds words to specific feature subspaces; (3) Fourier frequency-encoded routing enabling cross-modal signal targeting; and (4) a human-in-the-loop (HITL) conflict detection mechanism. Experiments on small fruit/object datasets show positive retrieval results against offline and online baselines.

---

## Rebuttal Assessment

### Weakness 1: HITL interaction never actually evaluated
- **Author's response:** Partially address
- **Assessment:** Partially convincing — The authors correctly point out that the full positive/negative learning logic is formally specified in Section 3.5 (Cases 1–3), and this is verified in the paper. Indeed, Case (1) explicitly states: *"If the user inputs a positive answer... N_m^V is added... If the user inputs a negative answer... N_m^V is not added."* However, the reviewer's core complaint was not that the logic is unspecified—it is that in every single experiment, Section 4 line 240 states: *"if the question posed to the user by OLM remains unanswered for a certain period of time, we set the answer to be positive,"* making the branching logic a dead letter in all reported results. The conflict detection claim ("OML is able to detect all conflicts and raise appropriate questions") remains a single sentence with no precision/recall numbers, no noise-rate sensitivity, and no experiment showing differential learning outcomes between positive and negative answers. The author acknowledges all this explicitly, calling it a gap and committing to adding the experiment—which is a future promise, not current evidence. The specification in Section 3.5 was already visible to the original reviewer; it does not constitute new evidence.
- **Score impact:** Weakness unchanged

### Weakness 2: No ablation study
- **Author's response:** Partially address
- **Assessment:** Partially convincing — The author argues that Table 2 ablates reference extraction (ART/AEN lack it) and Table 3 ablates frequency routing (AEN lacks λ). Both claims are verified in the paper: Section 4.1(2) explicitly states ART and AEN "cannot learn a precise referring" while OML can, and Section 4.1(3) confirms AEN "cannot distinguish whether a word refers to a taste or visual concept" while OML uses λ to solve this. However, this "ablation by proxy" is imperfect because ART and AEN are fully different architectures—not OML variants with components removed. The performance gaps could arise from multiple co-varying differences, not from the specific missing component alone. More importantly, three core components remain entirely unablated: the lateral pathways, the Gaussian descending thresholding (Eq. 2/4), and the OIAM/ODAM distinction. The author commits to adding a dedicated ablation table in the revision—again, a future promise.
- **Score impact:** Weakness downgraded (from "impossible to determine contributions" to "three key components ablated indirectly, three others still unablated")

### Weakness 3: Evaluation metric ambiguous
- **Author's response:** Partially address
- **Assessment:** Partially convincing — The author clarifies the metric is top-1 accuracy, which is consistent with Section 4.1's description of retrieving the highest-activated concept neuron. The paper's description ("we use one channel input to get outputs from other channels") does support a top-1 interpretation. However, this clarification is in the rebuttal, not in the paper itself—it is still not formally defined in the experimental setup section. The weakness exists in the paper as submitted, even if the intended metric is defensible.
- **Score impact:** Weakness downgraded (intent is plausible, but paper still lacks explicit definition)

### Weakness 4: Small-scale, narrow experimental footprint
- **Author's response:** Acknowledge
- **Assessment:** Unconvincing as a rebuttal — The authors honestly acknowledge the limitation, framing it as "future work." This is accurate but does not diminish the weakness. The paper remains evaluated on two small fruit/object datasets with handcrafted Fourier and MFCC features.
- **Score impact:** Weakness unchanged

### Weakness 5: Threshold parameters set without justification
- **Author's response:** Partially address
- **Assessment:** Partially convincing — The author correctly notes that θ is not a fixed constant but is set adaptively as "a quarter of the 2-norm of the weight of the neuron" (verified in Section 4). This is a genuine correction: the original review characterized θ as a fixed global constant, which was inaccurate. However, ϑ = 0.8 and r = 0.5 remain unjustified beyond handwavy arguments ("standard conservative choice," "typically large contrast"). No sensitivity analysis exists in the paper.
- **Score impact:** Weakness downgraded (θ is adaptive, reducing one concern; ϑ and r still lack ablation)

---

## Strengths

- **Online learning without catastrophic forgetting (Table 1):** In the open environment, OML achieves 89.8% on Fruits V→A versus AEN's 86.2%, directly validating continuous learning. Offline methods drop to as low as 52.3% (DAE) in the open setting.
- **Reference extraction for precise word-feature binding (Table 2):** OML achieves 87.8% on E-Fruits Open V→A versus AEN's 84.1% and offline methods dropping by 5–15% compared to Table 1, empirically supporting the coefficient-of-variation heuristic's effectiveness in isolating referred feature dimensions.
- **Modal extensibility (Table 3):** OML outperforms AEN across all 12 cross-modal tasks after integrating a taste channel, demonstrating that the frequency-tagged routing (λ) correctly segregates taste and visual concepts.
- **Architecturally coherent and technically detailed:** The Fourier-based routing mechanism (Eq. 1, 6) provides a clean mechanism for descending signal targeting; Section 3.1–3.5 maintain internal consistency throughout.
- **HITL logic is fully specified:** Section 3.5 Cases (1)–(3) correctly defines what happens under both positive and negative user responses—the mechanism is not merely claimed, it is formally described.

---

## Weaknesses

### Fatal
None.

### Major

- **HITL interaction is never empirically evaluated.** The paper's primary distinguishing contribution—interactive conflict resolution—defaults every user response to positive in all experiments (Section 4, line 240). Section 3.5 contains the full specification of both positive and negative response handling, but specification is not evaluation. No experiment measures whether the network's learned associations change under negative versus positive answers, and the conflict detection capability is asserted in a single sentence with no precision/recall metrics, no noise-rate sensitivity (only 10% injection tested), and no comparison to a no-HITL baseline. Given that HITL appears in the paper's title and throughout the introduction as the primary motivation, the absence of any differential-outcome experiment is the paper's decisive empirical gap.

- **Ablation coverage remains incomplete.** While the author argues Tables 2 and 3 serve as partial ablations via AEN/ART comparison, this is ablation by proxy rather than controlled component removal. The lateral pathways, Gaussian descending thresholding (ϑ), and OIAM/ODAM separation—components with non-trivial implementation effort—have no independent validation.

### Minor

- **Evaluation metric not formally defined in the paper.** The metric is likely top-1 accuracy based on the paper's description of retrieval, but it is never stated explicitly in the experimental setup. The rebuttal's clarification is informative but not present in the paper as submitted.

- **Small-scale, narrow experimental footprint.** All experiments use two small fruit/object datasets with handcrafted Fourier, color boundary, and MFCC features. No experiment tests the architecture with learned (e.g., deep) representations or larger category vocabularies. Scalability is entirely unaddressed.

### Trivial

- **ϑ = 0.8 and r = 0.5 lack sensitivity analysis.** θ is now confirmed adaptive (mitigated), but ϑ and r are stated without justification or ablation. The rebuttal's arguments for their robustness are verbal rather than empirical.

---

## Nice-to-Haves

- Add at least three controlled HITL conditions (always positive, always negative, 50% correct) and measure whether learned associations and retrieval accuracy differ across conditions.
- Report conflict detection precision and recall at multiple noise injection rates (5%, 10%, 20%).
- Add a 4-row ablation table (remove lateral pathways; remove reference extraction; remove Gaussian descending threshold; full OML) on E-Fruits Open V→A.
- State the evaluation metric explicitly in the experimental setup section.
- Add a sensitivity table for ϑ and r.

---

## Novel Insights

The coefficient-of-variation approach to reference extraction is the paper's most interesting technical contribution: by tracking which feature dimensions remain stable (low CoV) across training examples associated with the same word, the network autonomously discovers which modality subspace the word refers to, enabling principled separation of name-words from color attribute-words. This is empirically supported by Table 2 and is conceptually distinct from standard multimodal methods that treat all feature dimensions uniformly. The Fourier frequency-tagging approach for routing signals through the correct descending pathways is a neat and biologically motivated engineering choice that sidesteps the need for explicit modality labels. Both mechanisms are original and, if extended with richer feature representations and a proper ablation framework, would constitute a meaningful contribution to compositional multimodal grounding.

---

## Suggestions

1. Replace the default-positive simulation with at least three controlled conditions (always positive, always negative, random); show that learning outcomes differ. This is necessary to validate the paper's title claim.
2. Add conflict detection precision/recall at multiple noise injection rates (5%, 10%, 20%) to characterize detector operating characteristics beyond the single "all conflicts detected" assertion at 10%.
3. Add a controlled ablation table on E-Fruits Open V→A removing: (a) lateral pathways, (b) reference extraction, (c) Gaussian descending threshold, (d) OIAM/ODAM vs. uniform UAN.
4. Formally define the evaluation metric in the experimental setup section and consider adding mAP or Recall@k.

---

## Score and Decision

**Rebuttal impact assessment:**  
The rebuttal was honest and correctly identified which claims are and are not supported. However, honestly acknowledging a weakness does not remove it—the HITL evaluation gap, which is the paper's central contribution, remains entirely unaddressed by actual experiments. The author points to Section 3.5's specification (which the reviewer had already read), correctly notes that θ is adaptive (a minor correction), and argues Tables 2/3 serve as proxy ablations (valid but incomplete). The most the rebuttal achieves is: (a) downgrading the threshold weakness slightly (θ is adaptive), and (b) confirming that Tables 2/3 provide partial ablation evidence for reference extraction and frequency routing. These gains are insufficient to change the major weaknesses.

The paper falls in the 4.5–5.0 range based on anchor calibration: original architecture with real contributions (reference extraction, modal extensibility, online forgetting resistance), but the primary claimed contribution (HITL) is evaluated only with a vacuous positive-default fallback, ablations cover fewer than half the components, and the experimental scale is limited.

The rebuttal does not reveal that the original review was too harsh; it confirms the original assessment is accurate. The score remains at **4.5**.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>