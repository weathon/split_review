# Extend Model Merging from Fine-Tuned to Pre-Trained Large Language Models via Weight Disentanglement

- Decision: Reject
- Avg Score: 5.67
- Scores: 6, 6, 5

## Abstract
Merging Large Language Models (LLMs) aims to amalgamate multiple homologous LLMs into one with all the capabilities. Ideally, any LLMs sharing the same backbone should be mergeable, irrespective of whether they are Fine-Tuned (FT) with minor parameter changes or Pre-Trained (PT) with substantial parameter shifts. However, existing methods often manually assign the model importance, rendering them feasible only for LLMs with similar parameter alterations, such as multiple FT LLMs. The diverse parameter changed ranges between FT and PT LLMs pose challenges for current solutions in empirically determining the optimal combination. In this paper, we make a pioneering effort to broaden the applicability of merging techniques from FT to PT LLMs. We initially examine the efficacy of current methods in merging FT and PT LLMs, discovering that they struggle to deal with PT LLMs. Subsequently, we introduce an approach based on \textbf{W}e\textbf{I}ght \textbf{D}is\textbf{EN}tanglement (WIDEN) to effectively extend the merging scope, which first disentangles model weights into magnitude and direction components, and then performs adaptive fusion by considering their respective contributions. In the experiments, we merge Qwen1.5-Chat (an FT LLM with instruction-following skills) with Sailor (a PT LLM with multilingual abilities) across 7B and 14B model scales. Results reveal that: (1) existing solutions usually fail when merging Sailor, either losing both abilities or only retaining instruction-following skills; (2) WIDEN successfully injects the multilingual abilities of Sailor into Qwen1.5-Chat and make it proficient in Southeast Asian languages, achieving enhancements in the fundamental capabilities. In light of previous research, we also merge multiple 13B FT LLMs and observe that WIDEN achieves a balanced amalgamation of instruction following, mathematical reasoning, and code generation skills.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
Merging multiple LLMs, particularly those with substantial parameter shifts from pre-training (PT), presents challenges for traditional merging methods. To address this issue, the paper introduces WIDEN (Weight Disentanglement), a novel approach for merging large language models (LLMs) that have undergone either fine-tuning (FT) or pre-training (PT). This method expands the applicability of model merging beyond conventional fine-tuned models.

### Strengths
1. The paper makes a valuable contribution by identifying a critical limitation in existing model merging methods: their ineffectiveness when applied to continually pre-trained (PT) models. This insight is essential, as it highlights a gap in current merging techniques, which are generally only effective for fine-tuned (FT) models with minimal parameter shifts.
2. The paper introduces WIDEN (Weight Disentanglement), an innovative method that automatically computes the importance of weights during the merging process. WIDEN disentangles each model’s weights into magnitude and direction components, and then adapts the merging decisions based on the divergence of these components from a shared backbone. This approach removes the need for manually assigning scaling factors and effectively addresses the challenges posed by the varied parameter changes in both fine-tuned (FT) and pre-trained (PT) models.
3. The experimental results demonstrate that WIDEN outperforms existing merging methods by effectively combining both instruction-following and multilingual capabilities. The paper also evaluates WIDEN in traditional FT-only merging scenarios, where it achieves competitive performance compared to established methods.

### Weaknesses
1. The paper assumes that continually pre-trained (PT) models inherently experience larger weight shifts than fine-tuned (FT) models, which serves as the justification for a new merging approach. However, this assumption may not hold universally, as the degree of weight change in PT models depends on factors such as the data domain and dataset size. This raises questions about the paper’s motivation and the general applicability of its problem formulation. A more thorough exploration or empirical verification of weight changes across PT and FT models would help substantiate this claim. The authors are expected to provide empirical evidence comparing the distribution of weight changes between PT and FT models across different domains, model sizes, and dataset sizes. Specifically, the paper should analyze the variance in weight changes, not just the range, to understand the distribution's shape and its implications for the proposed method. Furthermore, the analysis should consider the impact of different pre-training objectives on the magnitude and direction of weight shifts.
2. The proposed ranking mechanism in WIDEN calculates divergences in magnitude and direction separately for each weight relative to the backbone model. However, the reliability of comparing magnitudes across models with different directional vectors is questionable. When calculating magnitude differences, direction is not considered, meaning that the importance of weights in different models could be misinterpreted if their directions diverge. Similarly, comparing directional differences might be misleading if the corresponding magnitudes differ significantly between models. So, have the authors considered alternative approaches that jointly consider both magnitude and direction? Additionally, have the authors empirically analyzed how often misinterpretation occur in practice due to treating these components separately? The paper should include a more detailed analysis of the correlation between magnitude and directional changes and how this correlation affects the merging process. It would be beneficial to explore methods that consider the vector nature of the weights, such as calculating the angle between weight vectors, rather than treating magnitude and direction as independent scalars.
3. Although WIDEN is intended to be a general merging technique applicable to both FT and PT models, its performance in merging FT models is comparatively weak (as shown in Table 5). Given that the method is designed to be adaptable across model types, this underperformance raises concerns about its overall efficacy. Are there certain characteristics of FT models that WIDEN struggles with? The paper should investigate whether the disentanglement of weights into magnitude and direction is necessary for FT models, or if a simpler approach would be more effective. A comparison of WIDEN with and without disentanglement on FT models would be valuable.
4. The experiments primarily focus on merging a specific PT model (Sailor) with a FT model, which limits the generalization ability of the results. Evaluating WIDEN on other PT models, particularly in diverse domains such as finance or healthcare, would provide stronger evidence of its effectiveness. The paper should also explore the impact of merging models with varying degrees of pre-training, as the current experiments only consider a single PT model with a substantial amount of pre-training. It would be valuable to assess how WIDEN performs when merging models with more subtle differences in pre-training.

### Questions
1. Equation 1: The shape of mD is equal to that of W. This equation should be corrected.
2. Equation 7: Could you provide a reason for not averaging all the differences by multiplying by 1/N?
3. Have the authors considered an alternative approach that compares each weight matrix on a column-by-column basis between the tuned model and the original backbone? Specifically, this approach would involve calculating and ranking differences column by column, rather than disentangling weights into separate magnitude and direction components.
4. How to grid search the hyperparameters for baselines methods? What validation dataset is used?
5. The paper should provide a figure to visually illustrate the proposed method.

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper presents a pioneering effort in extending model merging to Pretrained LLMs utilizing weight disentanglement. Extensive studies on previous methods demonstrate their inability to perform when applied to pretrained LLM while the method proposed in the paper is able to solve the task with minimal performance drop compared to the models to be merged.

### Strengths
1. The paper is the first successful attempt to incorporate the ability of PT LLM into model merging techniques.
2. Extensive experiments and analyses have demonstrated the effectiveness of the proposed method.
3. The paper is well-written and easy to follow.

### Weaknesses
1. The experiments are only limited to Sailor, more results on different models could validate the effectiveness of the proposed method.
2. Despite being indicated by the method, the experiments didn't show evidence that the proposed method could work for multiple LLM cases. Some experiments from this perspective would be appreciated.

### Questions
See weaknesses.

I'm not familiar with LLM merging and am open to discussion if misunderstood any part of the paper.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper presents WIDEN, a novel merging technique for Large Language Models (LLMs), which extends the applicability of merging from finetuned (FT) to pretrained (PT) models by disentangling weights into magnitude and direction components. This weight disentanglement enables adaptive merging by quantifying each LLM's alteration relative to a shared backbone. The disentangled weights are ranked using normalized divergence scores compared to the pretrained baseline, and this ranking is used to compute an automated importance factor for each LLM. This results in a generalized form of several existing arithmetic methods for LLM merging. Experimental results suggest that WIDEN effectively balances multiple capabilities, such as multilingual and instruction-following skills, across FT and PT LLMs.

### Strengths
- The paper’s effort to expand merging capabilities from FT to PT models is well-motivated and addresses a crucial gap in existing merging techniques.
- The methodology has a sound technical foundation, with a detailed four-step framework integrating weight disentanglement, ranking, and adaptive score calibration.
- The experimental setup is thorough, covering both conventional FT merging tasks and the new FT-PT merging setting. WIDEN’s performance across SEA and Open LLM Leaderboard benchmarks and comparison with multiple baselines highlights its applicability to diverse LLMs.
- The impact of each component within WIDEN is evaluated with an ablation experiment in Figure 2, demonstrating the importance of weight disentanglement and score calibration.

### Weaknesses
 - Although WIDEN generalizes across FT and PT models, it does not consistently outperform Task Arithmetic on all benchmarks. For instance, Task Arithmetic often shows competitive results on Open LLM Leaderboard tasks, raising concerns about WIDEN’s scalability and stability. For example, on the SEA benchmark, the performance improvement on 14B models is smaller than the 7B model, with the gap between Task Arithmetic and its claimed generalized form WIDEN narrowing as the LLMs become larger.
- The improvement WIDEN demonstrates is noticeably higher on SEA benchmarks than on the OpenLLM Leaderboard, yet the paper does not clarify why performance fluctuates between benchmarks. This omission raises questions about its adaptability to different domains or task settings. The lack of analysis regarding the specific characteristics of each benchmark and how they interact with WIDEN's merging strategy makes it difficult to assess the method's robustness.
- While grid search is used for tuning, the choice of hyperparameters (particularly t and s) lacks justification beyond empirical results. A clearer rationale or theoretical insight into their selection would enhance the robustness of WIDEN’s methodology. The paper does not provide sufficient explanation of how these parameters influence the merging process, making it difficult to understand the method's behavior under different conditions.
- Although score calibration is a novel addition to ensure adaptive ranking and merging, values other than 1.0 should be evaluated in score calibration. The "ease of implementation" rationale is not good enough. The paper should provide a more thorough exploration of the impact of different calibration values on the final performance, as this is a key component of the proposed method.

### Questions
- How does WIDEN handle cases where the backbone (reference pretrained model) diverges substantially in structure or task specificity from both FT and PT models? Would WIDEN work with heterogeneous LLMs beyond those sharing the same backbone?
- Did the authors attempt to merge more than two or three models to evaluate WIDEN’s scalability and robustness? If so, what were the results, and how does performance change as the number of LLMs increases?
- Given WIDEN’s better performance on SEA benchmarks than on the OpenLLM Leaderboard, could the authors elaborate on why this discrepancy exists? Is WIDEN more suited to particular types of tasks or linguistic benchmarks?
- On tasks where Task Arithmetic performs better, why might WIDEN’s performance lag?
- Since WIDEN modifies weights adaptively, would it be feasible to incorporate it into a continual learning setup where multiple LLMs are progressively merged over time? Could this method be used for models other than LLMs?

### Soundness
3

### Presentation
2

### Contribution
2
