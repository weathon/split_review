## Human Reviewer 1

### Summary
The paper targets test-time adaptation (TTA) under long-tailed (LT) test streams for vision–language models (VLMs). It proposes a three-part framework: Synergistic Prototypes (DP+EP) for representation retention, Rebalancing Shortcuts (RSs) with a clustering re-allocation loss for structural balance, and Balanced Entropy Minimization (BEM) to reduce optimization bias toward head classes.

### Strengths
- Addresses a practically important setting (LT streams in online TTA).

- Clear, modular design with complementary roles (representation / structure / optimization).

### Weaknesses
- (Major) Problem novelty/positioning. The failure modes (head-bias accumulation, tail erosion under EM) are not VLM-specific; they are general LT-TTA issues. While packaging under “VLM LT-TTA” is useful, the problem statement and the proposed mechanisms (prototypes, rebalancing, entropy shaping) appear modality-agnostic, not specific to VLM. The paper should (i) sharpen what is uniquely VLM (e.g., cross-modal drift, text prior effects) and show where L-TTA leverages that, or (ii) reframe as a general LT-TTA method and broaden evidence beyond VLMs.

- Model capacity: Results rely on low-capacity VLMs; validating on more powerful, recent VLMs (both open- and closed-source) would better establish its contribution and clarify whether gains persist or diminish with stronger backbones.

### Questions
- What concrete VLM-specific factors make LT-TTA harder than unimodal LT-TTA (e.g., cross-modal prototype drift, text prior effects)? Can you show cases where your gains require the VLM setup? (See Weakness 1)
- Any results with larger/stronger VLMs? (See Weakness 2)

### Soundness
3

### Presentation
3

### Contribution
2

### Rating
4

### Confidence
4

---

## Human Reviewer 2

### Summary
The paper introduces Long-Tailed Test-Time Adaptation (L-TTA), a new paradigm that explicitly addresses class imbalance during test-time adaptation of vision-language models. L-TTA focuses on real-world settings where data follow long-tailed distributions, and it consists of three key components: Synergistic Prototypes, Rebalancing Shortcuts, and Balanced Entropy Minimization. Extensive experiments on 15 long-tailed datasets show consistent gains in both accuracy and macro-F1, particularly for tail class.

### Strengths
S1. **Realistic problem formulation.** 
The paper is the first to define long-tailed test-time adaptation explicitly, bridging TTA and class-imbalance research. 

S2. **Theoretical support.**
The authors provide a proposition showing that BEM reduces the optimization gap between head and tail classes, giving analytical depth to their design.

S3. **Comprehensive experiments.** 
Evaluations across 15 datasets and diverse settings (OOD, domain shift, noise) demonstrate robustness and clear macro-F1 improvements, validating that the method indeed benefits rare classes.

### Weaknesses
W1. **Limited methodological novelty.**
While the paper defines a new and realistic long-tailed test-time adaptation setting, most of its core components --dual prototypes, rebalancing modules, and entropy regularization -- are adapted from existing long-tailed learning techniques. Therefore, the methodological contribution appears somewhat incremental, as it primarily repurposes well-known ideas rather than introducing fundamentally new mechanisms. Nevertheless, the adaptation of these ideas to a label-free, online TTA scenario is well-executed and empirically validated.

W2. **Computational overhead not fully analyzed.** 
In a test-time adaptation (TTA) environment, it is crucial to evaluate computational overhead, as most prior works explicitly report their runtime and justify that their methods can operate under realistic TTA constraints. To the best of my knowledge, the proposed method introduces additional parameters compared to existing baselines due to the inclusion of the RS module and dual prototypes. Therefore, a detailed analysis of runtime and memory consumption is required.

W3. **Hyperparameter sensitivity.** 
The method relies on several new hyperparameters (i.e., $\beta$ in BEM, $\tau$ for temperature, $\eta$ for CRA weighting). The paper gives fixed settings but limited analysis on sensitivity or tuning difficulty. 

W4. **Intuition of synergy of SyPs and RS.** 
The authors show the synergy of SyPs and RS with empirical results, but I cannot catch the intuition why those two modules can have positive synergy. Deeper explanation could make reviewers understand easily.

### Questions
Q1. In realistic streaming scenarios, the head/tail imbalance may continuously shift over time. For instance, some tail classes may gradually become head classes as data distribution evolves. How would L-TTA behave under such dynamic imbalance transitions? Would its components (e.g., BEM or RSs) still maintain stability and prevent bias accumulation when the head and tail relationship itself changes over time?

Q2. The proposed Synergistic Prototypes (SyPs) employ two prototypes per class to enhance representation learning for tail classes.
Have the authors considered extending this idea to an adaptive or variable number of prototypes per class, which could further capture intra-class diversity and prevent overfitting to limited modes within each class?

### Soundness
3

### Presentation
3

### Contribution
3

### Rating
6

### Confidence
4

---

## Human Reviewer 3

### Summary
This paper presents the Long-Tailed Test-Time Adaptation (L-TTA) framework, which addresses the performance degradation of vision-language models in test-time adaptation scenarios where the test distribution is long-tailed. Standard TTA methods typically amplify bias toward dominant classes, thereby harming underrepresented ones.
To solve this, they propose a complex, three-part system:   

- Synergistic Prototypes (SyPs): A dual-prototype memory system to separately accumulate confident (Deterministic) and improbable (Exclusionary) features, designed to enrich tail class representations.   
- Rebalancing Shortcuts (RSs): Learnable cross-attention adapters to dynamically balance the prototypes, optimized with a novel Class Re-Allocation loss.   
- Balanced Entropy Minimization (BEM): A new loss function that gates the influence of class priors using prediction confidence, specifically to protect tail classes from the over-optimization of head classes.   

Extensive experiments demonstrate that L-TTA achieves strong generalization and outperforms existing methods under a wide range of long-tailed test settings.

### Strengths
1. First work to formally study long-tailed test-time adaptation for VLMs, addressing a realistic yet overlooked deployment scenario.
2. Introduces a coherent three-part novel system (SyPs, RSs, BEM) with each component targeting a specific weakness of standard TTA under imbalance.
3. Outperforms 7 baselines across 15 datasets in accuracy and macro-F1, under different imbalance ratios. Gains are consistent on OOD, cross-domain, and noise benchmarks.
4. Achieves competitive adaptation speed without full-model optimization, making the approach practical for real-world use.
5. Provides thorough ablations and sensitivity studies showing the contribution of each component.

### Weaknesses
1. The method requires tuning several per-dataset hyperparameters, which contradicts with the core objective of test-time adaptation, where models are expected to generalize without dataset-specific tuning.
2. The Balanced Entropy Minimization (BEM) loss depends on access to class priors ($\pi$), which are not typically available in reality, making this assumption impractical.
3. This paper primarily emphasizes entropy-minimization, prompt-tuning, and prototype-based approaches, but it omits discussion of important emerging TTA families, such as vision-encoder adaptation methods (e.g., CLIP-ArTT[1], WATT[2]), parameter-free approaches (e.g., ZERO[3]), and reinforcement-based TTA frameworks (e.g., RLCF[4]).
4. The notation and exposition can be difficult to follow, and parts of the method are challenging to comprehend. Clarity and narrative coherence could be improved to enhance readability.

**Refs: 

[1] Hakim, Gustavo A. Vargas, et al. "Clipartt: Adaptation of clip to new domains at test time." WACV'25.

[2] Osowiechi, David, et al. "WATT: Weight average test time adaptation of CLIP." NeurIPS'24.

[3] Farina, Matteo, et al. "Frustratingly easy test-time adaptation of vision-language models." NeurIPS'24.

[4] Zhao, Shuai, et al. "Test-Time Adaptation with CLIP Reward for Zero-Shot Generalization in Vision-Language Models." ICLR'24

### Questions
1. Does the model still outperform baselines when using a consistent set of hyperparameters across datasets? Demonstrating this would help confirm that the performance gains are not dependent on per-dataset tuning. A positive result here would increase my evaluation score.
2. How does the model perform on balanced datasets? It would be helpful to see whether the proposed design adversely affects performance when the class distribution is uniform.
3. Can the authors report performance on additional corruption types (e.g., blur, snow, JPEG compression)? I recognize the rebuttal timeline is limited, but even small-scale experiments would strengthen the evidence of robustness across diverse corruption scenarios.

Finally, I remain open to adjustments or clarifications addressing the weaknesses raised in weaknesses section.

### Soundness
3

### Presentation
2

### Contribution
3

### Rating
4

### Confidence
3

---

## Human Reviewer 4

### Summary
This paper proposes L-TTA (Long-Tailed Test-Time Adaptation), a method for adapting vision-language models (VLMs) to long-tailed, unlabeled test distributions. The framework integrates three components—Synergistic Prototypes (SyPs), Rebalancing Shortcuts (RSs), and Balanced Entropy Minimization (BEM)—to mitigate head-class dominance during TTA. Experiments on 15 datasets show consistent gains over recent TTA baselines such as DPE and SCAP under class-imbalanced setups.

### Strengths
1. The paper is nicely organized, with convincing visuals and comprehensive benchmarks.
2. Evaluation across multiple datasets and metrics demonstrates the robustness of L-TTA.
3. The ablation study on components supports the effectiveness of SyPs, RSs, and BEM.

### Weaknesses
1. The “long-tailed TTA” setting largely overlaps with non-i.i.d. TTA explored in prior works such as LAME [a], NOTE [b], SAR [c], DA-TTA[d], and DELTA [e]. The challenges analyzed (imbalance over time, EM bias, boundary collapse) are identical to those already studied in non-i.i.d. test-stream TTA. Therefore, I doubt the claim that this is the “first study of TTA under long-tailed scenarios.” The authors may need to demonstrate the conceptual or procedural difference more clearly.
2. Because of the overlap mentioned above, the proposed method also appears similar to existing ones. BEM modifies EM by adding a penalty that down-weights already-confident classes to reduce head-class over-optimization. This seems very close to class reweighting in non-i.i.d. TTA (e.g., DELTA), which injects class-wise weights to counter imbalance during EM. As written, Propositions 1–2 provide intuition but not a decisive distinction from prior class-aware EM approaches, which makes this component appear incremental rather than novel.
3. Section 2 lacks explicit discussion of non-i.i.d. TTA. Adding a subsection contrasting L-TTA with these prior studies is essential for proper positioning.
4. Table 4 omits training-free TTA methods for VLMs (e.g., TDA, ZERO [f]), which are critical for comparisons in speed/accuracy trade-offs.

[a] Parameter-free online test-time adaptation. CVPR 2022.\
[b] Note: Robust continual test-time adaptation against temporal correlation. NeurIPS 2022.\
[c] Towards stable test-time adaptation in dynamic wild world. ICLR 2023.\
[d] Distribution alignment for fully test-time adaptation with dynamic online data streams. ECCV2024.\
[e] Delta: Degradation-free fully test-time adaptation. ICLR2023. \
[f] Frustratingly Easy Test-Time Adaptation of Vision-Language Models. NeurIPS2024.

### Questions
1. How is the long-tailed TTA setting formally different from non-i.i.d. TTA? Could the authors provide a side-by-side comparison of assumptions and experimental protocols?
2. How does BEM differ empirically from previous class-weighted EM variants such as in DELTA [e]?

### Soundness
3

### Presentation
3

### Contribution
2

### Rating
6

### Confidence
4