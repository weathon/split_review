Now I have a complete picture of both the paper and the reviewer inputs. Let me synthesize the final review.

---

## Summary

This paper proposes OML, a brain-inspired hierarchical neural network for online multimodal learning that can continuously learn new concepts without catastrophic forgetting, extract precise feature references for words (e.g., that "red" refers to color dimensions, not shape), and detect conflicts with previously learned knowledge while querying users for resolution. The architecture comprises feature neurons with Fourier-based frequency routing, unimodal and multimodal association neurons, and ascending/descending/lateral pathways, evaluated on fruit/object datasets against both offline and online baselines.

---

## Strengths

- **Online learning without catastrophic forgetting**: In the open environment (four-partition sequential learning), OML achieves 89.8% (V→A, Fruits) and 89.0% (A→V, Fruits) while online competitors ART and AEN achieve 84.2%/86.2% and 83.0%/84.9%, respectively (Table 1). The stability across sequential partitions is consistently demonstrated.

- **Precise reference extraction**: On the enhanced datasets (E-Fruits, E-HomeF), OML is the only method that does not suffer significant accuracy drops when color-referring words are added (Table 2 ↓-markers). For example, OML achieves 87.8% on E-Fruits open V→A vs. 84.1% for AEN and 75.0%–76.3% for offline methods — concretely validating the CoV-based reference extraction mechanism.

- **Frequency-coded cross-modal routing enables modality-specific recall**: The λ-parameterized descending pathway correctly routes "tián" (sweet) to the taste channel and "hóng sè" (red) to the visual channel, whereas AEN cannot distinguish between them (Section 4.1(3), Table 3). OML achieves 92.1% T→V open vs. AEN's 89.2%, supporting this architectural claim.

- **Seamless modal extensibility**: Adding a taste channel extends the visual-auditory network without retraining existing modules; Table 3 shows consistent improvements over AEN across all six cross-modal retrieval directions on VAT and VAT-HomeF, demonstrating the practical modularity.

---

## Weaknesses

### Fatal
None.

### Major

- **The human-in-the-loop mechanism — the paper's primary stated contribution — is not evaluated.** Section 4 explicitly states: "if the question posed to the user by OLM remains unanswered for a certain period of time, we set the answer to be positive." Every experiment therefore defaults user answers, making it impossible to assess whether the interaction system changes learning outcomes, handles negative answers correctly, or degrades gracefully under noisy user feedback. The paper's title, abstract ("If a conflict occurs, the network is capable of posing appropriate questions to the user and updating itself based on the user's answers"), and Section 1 attribute (2) frame this as a primary contribution. The conflict detection result is reported only as a single-sentence assertion ("OML is able to detect all conflicts") for a single 10% noise injection rate, with no precision/recall breakdown, no false-positive analysis, and no comparison of learning outcomes under positive vs. negative user answers. This is not an ablation preference — it is the foundational claim the paper is built on.

- **No ablation study for a heavily engineered multi-component system.** The architecture combines Fourier-based FN activation (Eq. 1), Gaussian descending activation thresholding (Eq. 2/4), CoV-based reference extraction (Eq. 7), ascending/descending/lateral pathways, OIAM vs. ODAM modes, and frequency routing (Eq. 6). None of these components are individually ablated. Performance in Tables 1–3 is attributed to the whole system; it is impossible to determine which components are responsible for the gains over AEN, or whether the complex Fourier encoding (Eq. 1) contributes beyond a simpler routing tag.

### Minor

- **The evaluation metric "accuracy" is undefined for a retrieval task.** The tasks (V→A, A→V, T→V, etc.) are described as using "one channel input to get outputs from other channels" (Section 4.1), but whether this is top-1 recall, rank-1 retrieval accuracy, or something else is never stated. Without this definition, the numbers in Tables 1–3 cannot be reproduced or compared to literature benchmarks.

- **Experimental scale is narrow.** All results are on two small-scale fruit/object datasets with handcrafted features (Fourier shape descriptors, mean color, MFCCs). Whether the growing-network architecture and CoV-based reference extraction generalize to larger vocabularies, diverse categories, or learned deep features is unaddressed. This limits confidence in the method's breadth.

- **Threshold values are stated without justification or sensitivity analysis.** ϑ = 0.8 (Eqs. 2, 4), r = 0.5 (Eq. 7), and θ = ¼||w|| (Eq. 1) are set without analysis. Since θ directly controls when conflicts are flagged and r controls reference extraction, small changes could substantially affect the core claims in Table 2 and the conflict detection result.

### Trivial

- Section 4.1(3) limits the Table 3 baseline to AEN alone ("Because only AEN deals with the modal extension problem"). ART is also an online method; the paper does not argue why it cannot be extended to a third modality. A brief justification would strengthen this choice.

---

## Nice-to-Haves

- A controlled simulation of user interaction — e.g., testing under always-positive, always-negative, and 50%-correct answer patterns — would be far more informative than the current default-positive fallback, and would not require a live user study.
- Direct visualization of the features extracted by the reference extraction algorithm (which dimensions are selected for name words vs. color words, across different samples and word types) would strengthen Section 3.4 beyond the qualitative Figure 3(a).
- A small ablation removing the lateral pathways, the descending activation, and the reference extraction module separately would make the contribution attributable and substantially strengthen the paper.

---

## Removed Points

*These points are flagged for removal; treat them with caution.*

- **Harsh Critic: "Comparison with offline methods inflates OML's advantage."** The paper explicitly frames the offline vs. online comparison as a demonstration of catastrophic forgetting, not as a claim of superiority over offline methods in general. The meaningful online-vs-online comparison (vs. ART and AEN) is present in all tables. The offline comparison illustrates a known limitation of a different paradigm. REMOVED per the asymmetric-comparison rule (the asymmetry favors baselines in the close environment, where offline methods score higher).

- **Harsh Critic: "Motivation for Fourier representation unexplained."** This is a nitpick about design explanation preference, not a defect in the method. The frequency routing is used operationally (to direct descending signals to the correct channel), and its function is demonstrated in Table 3. The absence of a comparative ablation is captured in the Major weakness above; separately criticizing the motivation would be duplicative. REMOVED as stylistic.

- **Harsh Critic: "ART could plausibly be extended to a third modality."** This is speculative. The paper's claim that only AEN specifically addresses modal extension (Xing et al. 2021) is not contradicted by anything in the paper. REMOVED as speculation not grounded in the paper.

- **Strength Finder: "Human-in-the-loop conflict detection is a confirmed strength."** Partially accepted: the paper does claim all conflicts were detected at 10% noise. However, the interaction component (updating from user answers) is not demonstrated, weakening this as a blanket strength. Retained only in attenuated form — conflict detection is claimed but unrigorously validated; the full HITL loop is not tested.

---

## Novel Insights

The CoV-based reference extraction mechanism (Eq. 7) is the paper's most distinctive and technically novel element: by monitoring which feature dimensions stabilize (low coefficient of variation) across training examples for a given word neuron, the system autonomously infers the feature type a word refers to. This is behaviorally motivated and empirically supported by the consistent Table 2 gains. The insight that word-concept grounding can be operationalized via variance tracking — without supervised feature annotation — is the paper's strongest contribution and is underemphasized relative to the human-in-the-loop framing.

---

## Suggestions

1. Conduct a controlled evaluation of the human-in-the-loop mechanism: inject 10%, 20%, 50% conflict rates, and simulate user responses at multiple accuracy levels. Measure how learning outcomes differ under positive vs. negative answers. This is the single highest-impact improvement.
2. Add a targeted ablation: (a) remove lateral pathways, (b) remove the reference extraction module (treat all features equally as AEN does), (c) remove descending activation. This would validate the architecture's individual contributions.
3. Define the retrieval metric precisely in Section 4; specify whether "accuracy" is top-1 recall over the test set, and report class sizes.
4. Provide a sensitivity curve for ϑ and r across a range of values to bound the robustness of the reported results.

---

## Score and Decision

**Originality**: The reference extraction mechanism is genuinely novel and cleanly motivated; the overall HITL-online-multimodal framing is a distinct problem setup. Score: 4/5.

**Importance**: Online multimodal learning with conflict resolution is underexplored and practically relevant; the problem statement is well-posed. Score: 4/5.

**Claims well-supported**: The online learning and precise referring claims are well-supported by Tables 1–2. The HITL interaction claim — prominently featured in the title and framing — is not evaluated beyond default-positive simulation. Score: 2/5.

**Soundness of experiments**: Results are consistent and the open-environment protocol is well-designed, but the missing ablations and undefined metric weaken experimental rigor. Score: 3/5.

**Clarity of writing**: The architecture description is detailed and the figures provide useful illustration; some notation is dense. Score: 3/5.

**Value to research community**: The method introduces a useful perspective on brain-inspired continual multimodal learning with reference grounding; the experimental gaps limit immediate reproducibility. Score: 3/5.

The paper contains genuine novelty (reference extraction, frequency routing for modality-specific recall) and solid evidence for two of its three major contributions. However, the third and most prominently framed contribution — human-in-the-loop interaction — is bypassed in all experiments through a default-positive fallback. Combined with the absence of any ablation for a heavily engineered system, the paper cannot substantiate its central claims in their current form.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>

<subscores>
<originality>4</originality>
<importance>4</importance>
<claims_supported>2</claims_supported>
<soundness>3</soundness>
<clarity>3</clarity>
<community_value>3</community_value>
</subscores>