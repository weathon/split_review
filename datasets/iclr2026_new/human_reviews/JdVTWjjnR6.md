## Human Reviewer 1

### Summary
This paper proposes Hippocampal–Thalamic dual-stream Network, a brain-inspired framework for multimodal sentiment analysis under frame-level missing data. 
The authors draw inspiration from two functional mechanisms of the human brain: 
(1) the hippocampal memory retrieval process, which reconstructs missing information through semantic association, 
and (2) the thalamic perceptual regulation process, which integrates multisensory inputs while filtering unreliable cues. 
Accordingly, HiTNet is composed of two complementary streams: 
a hippocampal-inspired intra-modal enhancement stream that employs semantic memory and sparse activation modules to recover modality-specific semantics, 
and a thalamic-inspired inter-modal regulation stream that utilizes confidence perception and adaptive cross-modal completion to integrate high-quality information across modalities. 
A hierarchical fusion module combines both streams for sentiment prediction.

### Strengths
1. Effectiveness
Experiments on three standard benchmarks (MOSI, MOSEI, and SIMS) demonstrate consistent improvements of 1.5–2.0% over state-of-the-art methods across various missing rates, 
and the model maintains 72.2% accuracy even under 90% missing data on MOSEI. 
Ablation and visualization studies further support the dual-stream design’s effectiveness and robustness.

2. Appealing
The proposed idea is intuitively appealing. The analogy between hippocampal memory reconstruction and thalamic regulation provides an intuitive, biologically inspired rationale that enriches the interpretability of multimodal fusion. The proposed HiTNet introduces a biologically motivated architecture that integrates hippocampal-style memory retrieval and thalamic-style perceptual regulation. This dual-stream formulation is conceptually novel in the context of multimodal sentiment analysis and offers an interpretable way to address missing-data challenges.

3. Good writing
The manuscript is well organized, with a coherent flow from motivation to methodology and experiments. Figures and tables are informative and contribute to the clarity of presentation.

### Weaknesses
1. Quantitatively realized
How the “hippocampal” and “thalamic” analogies are quantitatively realized. While the hippocampal–thalamic analogy is conceptually interesting, the connection to actual neuroscientific mechanisms remains largely metaphorical.

2. Computational overhead and scalability
Computational overhead and scalability of the memory and activation modules. The memory retrieval and sparse activation modules may introduce additional computational overhead. The paper would benefit from a quantitative analysis of training/inference cost and scalability to larger datasets.

3. Minor concerns
Refer to the questions

4. Biased dataset performance discussion
While HiTNet performs strongly on MOSI/MOSEI, the performance margin on SIMS is relatively modest.

### Questions
1. Inconsistent terminology formatting
The paper inconsistently uses “intra-modal” and “inter-modal” in some places, while elsewhere they appear as “intramodal” and “intermodal.” Please standardize the terminology throughout the manuscript for consistency and readability.

2. Inconsistent expression of ‘missingness’
The manuscript alternates between “modality missingness” and “modality missing.” Since “missingness” is the correct nominal form referring to the state or rate of missing data, it should be used consistently.

3. Noun form correction
In a few instances, “missing” is used as a noun, which is grammatically suboptimal. It would be more precise to use “missingness” in these cases.

4. Tense consistency in reproducibility statement
The sentence “We have made every effort to ensure that the results presented in this paper are reproducible.” mixes present perfect with simple present.

### Soundness
2

### Presentation
3

### Contribution
3

### Rating
6

### Confidence
3

---

## Human Reviewer 2

### Summary
This paper introduces HiTNet, a brain-inspired dual-stream network for MSA with missing data. The HiTNet includes an intra-modal enhancement stream that reconstructs missing features using semantic memory, and an inter-modal regulation stream that adaptively fuses reliable information across modalities. Experiments on MOSI, MOSEI, and SIMS show that HiTNet achieves SOTA accuracy, demonstrating its effectiveness.

### Strengths
1. The method is well-motivated and the overall model design is reasonable.
2. The experiments and analyses are comprehensive, demonstrating the method’s effectiveness.
3. The model achieves SOTA performance across multiple datasets.
4. The paper is well-written and easy to read.

### Weaknesses
1. How is the Top-K value in the Semantic Memory Module selected? Could the authors discuss the impact of different k values on performance?
2. The proposed method involves sparse activation across multiple modules. Could the authors analyze what would happen if full activation were used instead?
3. Could you add explanations for G and g in the caption of Figure 2, or include a legend directly in the figure for clarity.
4. The paper claims that Hierarchical Fusion provides better performance. Could you compare it against simpler alternatives such as concatenation, summation, or attention-based fusion?
5. Since the optimization objective includes many constraint terms, could this lead to unstable or slower training? Could you show training curves and discuss convergence behavior? In addition, how sensitive is the training process to random seed variations Does the loss fluctuate significantly?
6. In section relevant work, could you introduce and discuss all the methods you compared?

### Questions
Please see Weaknesses.

### Soundness
3

### Presentation
4

### Contribution
3

### Rating
6

### Confidence
5

---

## Human Reviewer 3

### Summary
The paper targets multimodal sentiment analysis under frame-level, asynchronous missing across text, audio, and visual streams. It introduces HiTNet, a hippocampal–thalamic inspired dual-stream architecture: an intra-modal (hippocampal) path that performs memory-based completion via a learnable semantic memory and sparse activation/routing to exploit residual evidence within each modality, and an inter-modal (thalamic) path that estimates per-modality confidence and performs confidence-gated cross-modal completion to import only reliable cues. The streams are hierarchically fused, with auxiliary reconstruction and regularizers for routing balance and confidence calibration. On MOSI, MOSEI, and SIMS, HiTNet consistently improves Acc/F1 and MAE/Correlation over strong baselines and shows slower degradation up to 90% missing, indicating robust reliability modeling. Ablations verify the necessity of semantic memory, confidence estimation, and the two-stream design.

### Strengths
1. Propose a dual-stream (hippocampus/thalamus) framework that decouples "intra-modal self-completion" and "inter-modal confidence regulation," resulting in clear and reusable functional boundaries.
2. Focusing on more realistic and common frame-level asynchronous missing data scenarios, rather than just complete modality absence, makes the research more meaningful.
3. By utilizing semantic memory and sparse routing, the paper first extracts all available evidence from the current modality, reducing over-reliance on other modalities and resulting in greater robustness.

### Weaknesses
1. This paper does not compare its method with some powerful modern imputation methods such as masked-autoencoding and diffusion-based completion. Also missing are ablations against simpler reliability heuristics (e.g., SNR/entropy-based gates). These methods may seem more suitable for scenarios where frames are missing.
2. The input with missing frames does not simulate real-world scenarios, such as consecutive frame drops due to packet loss. Conducting experiments under such conditions would be more convincing.
3. By coupling the intra- and inter-modal streams only via a late, single-point gate, the model limits cross-layer interactions and can miss fine-grained synergies that require earlier or multi-level fusion.
4. The convex mix $s⋅x+(1−s)⋅h$ assumes additive compatibility between native and completed features, risking blurred signals and underfitting of nonlinear cross-modal interactions.

### Questions
1. Could you provide an explanation for the performance of HiTNet and w/o $L_{ubl}$ in Table 3 in terms of acc-7 and acc-5?
2. Why couple the intra- and inter-modal streams only via a single late gate—did you evaluate earlier or multi-level fusion (e.g., MoE or cross-layer gating)?
3. Does using a single prompt token for each modality in cross-modal completion methods result in insufficient expressive power?
4. How do you handle the $O(T^2)$ complexity of attention mechanisms in long sequence scenarios (>1-5 minutes)?

### Soundness
2

### Presentation
2

### Contribution
2

### Rating
4

### Confidence
3

---

## Human Reviewer 4

### Summary
The paper addresses multimodal sentiment analysis under simultaneous random frame-level missing cues across modalities. It introduces HiTNet, a hippocampal–thalamic architecture with an intra-modal semantic memory that retrieves and updates residual signals via sparse activation for reconstruction, and an inter-modal regulation path that estimates modality confidence and performs confidence-aware cross-modal completion with learnable prompts, followed by hierarchical fusion. Experiments on standard benchmarks indicate consistent gains across missing rates and strong robustness even under extreme sparsity, with ablations showing that each component contributes materially. Overall, the problem is timely, the design is biologically inspired yet technically grounded, and the evidence suggests practical value.

### Strengths
1. The paper addresses a meaningful and insufficiently studied problem in multimodal sentiment analysis under random frame-level missing data, showing clear motivation and novelty.
2. The proposed HiTNet framework is well designed and coherent, combining hippocampal-inspired intra-modal memory with thalamic-inspired confidence-aware cross-modal completion to enhance robustness and information utilization.
3. The experimental evaluation is thorough and convincing, demonstrating consistent improvements across datasets and strong stability under severe missing conditions, with ablation results supporting each component’s effectiveness.

### Weaknesses
1. The biological inspiration, while interesting, remains mostly metaphorical; the paper could better justify how the hippocampal–thalamic analogy concretely guides the architecture design and contributes beyond naming.
2. The experimental section, though broad, lacks sufficient comparison with very recent multimodal robustness approaches or large foundation models, which limits understanding of its relative performance in the current landscape.
3. Some implementation details and hyperparameter settings are not clearly described, making it difficult to reproduce results or fully assess the method’s computational efficiency and scalability.

### Questions
1. How sensitive is the model’s performance to the design of the semantic memory module and the sparse activation mechanism? Would alternative memory retrieval or selection strategies yield similar robustness?
2. How well does HiTNet generalize to other multimodal tasks beyond sentiment analysis, such as emotion recognition or multimodal dialogue, especially when the missing patterns differ from those in the benchmarks?

### Soundness
3

### Presentation
2

### Contribution
3

### Rating
6

### Confidence
4

---

## Human Reviewer 5

### Summary
Inspired by findings in neuroscience, this paper proposes a multimodal sentiment analysis model named HiTNet, designed for scenarios with missing modalities. The model architecture is motivated by two functional mechanisms in the brain: the hippocampus, which is responsible for semantic memory retrieval and pattern completion, and the thalamus, which regulates perceptual integration and confidence control. Specifically: 1. The hippocampus performs semantic memory retrieval and pattern completion; 2. The thalamus dynamically integrates multimodal information and regulates reliability among modalities. The proposed HiTNet consists of two parallel subnetworks: an intra-modal enhancement stream and an inter-modal regulation stream. Experimental results demonstrate that HiTNet achieves superior performance on multiple datasets (MOSI, MOSEI, and SIMS), maintaining high accuracy even under conditions of severe modality missing.

### Strengths
1. The paper introduces the hippocampal–thalamic mechanism from neuroscience into multimodal sentiment analysis under modality-missing conditions. The idea is novel and demonstrates strong originality.

2. Experiments on three benchmark datasets validate the effectiveness of the proposed method. Comprehensive ablation studies are conducted for each module to verify their contributions, along with analyses on missing rates and loss weight settings, showing the experimental evaluation is thorough.

3. Compared with baseline models, the proposed method consistently outperforms existing approaches across all three datasets and under various missing ratios.

4. The paper is clearly written and well-structured, making it easy to follow.

### Weaknesses
1. The paper states that “the missing information reconstruction module ERec, designed to reconstruct the missing features of each modality,” but in Figure 2, the position of this module is ambiguous, making it difficult for readers to interpret and align it with the overall framework.

2. The paper does not explore the model’s performance under non-random missing scenarios.

3. There are some writing detail issues: the formulas lack proper punctuation — for example, a comma should follow Formula (2) and a period should follow Formula (3). Formula (7) should be followed by an explanatory sentence, and the use of uppercase and lowercase letters is inconsistent.

### Questions
1. In Tables 5 -7, only a few combinations of loss weights (α, β, γ) are tested (e.g., 15, 0.5, 0.1 and 10, 0.9, 0.1). Could you elaborate on how these specific values were chosen? Were they selected empirically, or do they correspond to particular design motivations (e.g., emphasizing one auxiliary loss over another)?

2. In the hierarchical fusion stage, the language modality is always placed last. Is the model sensitive to the order of modality fusion?

### Soundness
3

### Presentation
3

### Contribution
3

### Rating
6

### Confidence
2

---

## Human Reviewer 6

### Summary
The paper proposes HiTNet, a dual-stream network inspired by hippocampal memory retrieval and thalamic perceptual regulation for multimodal sentiment analysis under severe frame-level missingness. The “hippocampal” stream uses a key-value semantic memory module plus sparse activation sub-networks to reconstruct intra-modal features; the “thalamic” stream estimates per-modality confidence and performs adaptive cross-modal completion. A hierarchical Cross-Transformer fuses both streams and an auxiliary reconstruction loss is added.

### Strengths
- Originality: First work that explicitly models hippocampal pattern-completion and thalamic gating for frame-level missing data; combines key-value memory, sparse routing, and confidence-weighted cross-modal attention in a unified framework.

- Quality: Each component is formally described, ablated, and visualised.

- Clarity: Well-written; neuroscientific motivation is intuitive; notation is consistent.

- Significance: Addresses a practical and under-studied scenario (random frame-level corruption across all modalities) and demonstrates remarkable robustness at extreme missing rates that prior reconstruction or co-learning methods cannot reach.

### Weaknesses
- Novelty gap with existing memory-based completion: Key-value memory banks have been used for missing-modality imputation and for speech emotion with artefacts. The authors should clarify how their SMM differs from these works beyond simply being applied to sentiment.

- Biological inspiration is loose: The hippocampus performs associative pattern completion across time, whereas the SMM retrieves a single best-matching vector with cosine similarity and updates by frequency, which is closer to a standard dictionary. A more rigorous mapping or citation to computational neuroscience models (e.g., Hopfield networks, Kanerva’s sparse distributed memory) would strengthen the claim.

- Inference requires five sub-networks per modality, a memory bank of 64×3 tensors, two Transformers for confidence & completion, and a 4-layer fusion transformer. The paper reports accuracy but not latency, FLOPs, or GPU memory; a table or plot (e.g., vs. LNLN) is needed for deployment claims.

- Hyper-parameter sensitivity: Optimal loss weights differ by dataset (MOSI α=10, MOSEI α=1.5). No automatic tuning or principled weighting (e.g., uncertainty weighting, GradNorm) is explored, raising reproducibility concerns.

### Questions
1. Can you show one concrete example (frames + spectrogram + text) where intra-modal completion visually/audibly recovers lost content?

2. What happens under non-random missing patterns—e.g., consecutive video frames dropped due to buffering, or audio muted for the last 2 s? Does confidence prediction still help?

### Soundness
2

### Presentation
3

### Contribution
2

### Rating
2

### Confidence
3