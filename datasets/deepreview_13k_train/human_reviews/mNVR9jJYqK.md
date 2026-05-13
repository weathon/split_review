# DRESSing Up LLM: Efficient Stylized Question-Answering via Style Subspace Editing

- Decision: Accept
- Scores: 6, 6, 8, 5

## Abstract
We introduce DRESS, a novel approach for generating stylized large language model (LLM) responses through representation editing. Existing methods like prompting and fine-tuning are either insufficient for complex style adaptation or computationally expensive, particularly in tasks like NPC creation or character role-playing. Our approach leverages the over-parameterized nature of LLMs to disentangle a style-relevant subspace within the model's representation space to conduct representation editing, ensuring a minimal impact on the original semantics. By applying adaptive editing strengths, we dynamically adjust the steering vectors in the style subspace to maintain both stylistic fidelity and semantic integrity. We develop two stylized QA benchmark datasets to validate the effectiveness of DRESS, and the results demonstrate significant improvements compared to baseline methods such as prompting and ITI. In short, DRESS is a lightweight, train-free solution for enhancing LLMs with flexible and effective style control, making it particularly useful for developing stylized conversational agents. Codes and benchmark datasets are available at https://anonymous.4open.science/r/DRESS-LLM.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces DRESS, i.e., Disentangling Representation Editing in Style Subspace, a new approach for generating stylized responses from Large Language Models (LLMs) via representation editing. The core idea is to disentangle and edit within style-relevant subspaces of the LLM's representation space, enabling training-free style adaptation while preserving semantic meaning. Empirical results on the curated benchmark show that DRESS outperforms baselines including prompting, SFT, and other representation editing approaches.

### Strengths
- The proposed approach is well-motivated and intuitive. The approach has clear advantages over previous methods such as prompting and SFT.
- The training-free approach achieves superior performance compared to supervised fine-tuning, which shows the effectiveness of DRESS.
- The paper’s writing and presentation are clear and easy to follow.

### Weaknesses
 - The dataset construction process heavily relies on GPT-4 to collect the stylized responses, which could be limited and biased with GPT-4’s capability. Specifically, the potential for subtle semantic drift during the style transfer process is a significant concern. The reliance on a single model for generating both the base and stylized responses introduces a homogeneity that might not reflect real-world stylistic variations, potentially limiting the generalizability of the findings.
- The evaluation benchmark only considers two language styles, one for each language. This can be quite limited as it is not clear whether the approach can be well generalized to other styles. The choice of only two styles, particularly those from specific historical periods, raises questions about the method's robustness across a broader range of stylistic variations, such as modern dialects or genre-specific styles. The lack of diversity in styles tested makes it difficult to assess the true scope and limitations of the proposed approach.
- The evaluation task and the use case discussed in this work are also limited. The paper solely focuses on the stylized QA task. However, the effectiveness of style transfer or editing techniques should be proven under more realistic settings, such as conversation and more general user-AI interactions. The evaluation is confined to a narrow task, which does not fully capture the complexities of real-world applications where style transfer might be required in more dynamic and open-ended scenarios. The absence of evaluation in conversational settings or other interactive tasks limits the practical implications of the findings.
- The paper only applied Qwen-1.5-14B-Chat as the base LLM. It’s not clear whether the improvement and the conclusions can be generalized to other LLMs, such as LLaMA. The lack of experiments across different model architectures and sizes raises concerns about the method's general applicability. It is crucial to demonstrate that the proposed approach is not specific to a particular model and can be effectively used with other LLMs.

### Questions
- For the SFT baselines, have the authors also considered applying full finetuning? What would be the performance?
- Have the authors tried to apply the approaches to other sizes of LLMs? For example, what would be the results when you apply DRESS to a 7B/8B LLM?

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
3

### Summary
The paper introduce DRESS, a new method for making LLMs generate answers in specific style without need training. Main contributions:
* Propose style subspace editing technique that find and modify specific parts of LLM representations to control output style
* Use 3 key techniques: attention head filtering, style subspace filtering, adaptive editing strength
* Create 2 benchmark datasets (Shakespeare-style English, Dream of Red Chamber-style Chinese) for testing stylized QA
* Show better results than previous methods like prompting, fine-tuning, etc.

### Strengths
* The proposed approach is novel, interesting and intuitive, instead of traditional prompting/fine-tuning, they find and edit "style subspace" in LLM representations. This is more efficient because no training needed
* The paper has good theoretical foundation, they use concepts like orthogonality of representations and attention head functions to justify their method
* Implementation details are clearly presented in the paper, they explain exact math formulas and algorithms, make it easy to reproduce
* This paper conducted comprehensive experiments, which test on 2 very different language styles (English + Chinese), compare with strong baselines, use multiple evaluation metrics. The results look convincing, both automatic metrics and GPT-4 ratings show clear improvements over baselines

### Weaknesses
 * Need more analysis why method work better, authors show good results but don't explain deeply why style subspace editing is better than other approaches
* Some technical terms not explained well - like "style-relevant subspace", "adaptive editing strength" - need more intuitive explanation
* There are limited style types tested, only try 2 literary styles, should test more modern styles like formal/casual, different emotions, etc.
* Lacking of through discussion of limitations
* This paper's ablation studies are not enough - should test each component (attention filtering, subspace filtering, adaptive editing) separately to show importance

### Questions
Have you tried methods similar to knowledge editing?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
Stylized generation to reference style is an important problem in language generation. This paper introduces a new approach for stylized generation with LLM that differs from prompting and fine-tuning based approaches. To ensure that the generation quality is not compromised in the pursuit of stylized generation, the paper introduces the notion of steering vectors that is learnt by filtering the appropriate attention head that controls the style aspects of the generation and filtering the irrelevant style subspaces to minimize the impact on semantics while maximizing the impact on style. To evaluate the approach, the paper further introduces 2 benchmarks: Shakespeare style English QA and Dream of Red Chamber styled Chinese QA.

### Strengths
The approach is interesting and builds on top of existing works. There is a lot of value to the solution and the extensive evaluation is impressive.

### Weaknesses
Given the problem is being tackled by several researchers over the past few years, I would have loved to see more details on the "data hunger" of the proposed approach. For e.g., a prompting based approach requires only a few samples and if the current approach is only marginally better than that in qualitative comparisons, the value might be ambiguous. To this end, I would like to see a bit more detailed comparison along the lines of the data needs - which is critical to extend to low-resource style adaptation cases.

### Questions
Seen the weakness section above.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper introduces an approach for style transfer. The main motivation is to learn a style-relevant subspace, and then project the common language model space to this space to enable stylized response. This work is similar in spirit to different model editing papers for knowledge editing. The only difference is that here the style is more or less an implicit form of knowledge. The paper suggests that the model is lightweight, training-free in terms of the inference.

### Strengths
1. The paper is well written and clearly motivated.
2. The paper's approach is technically sound.
3. The evaluation seems to show improvement.

### Weaknesses
1. The approach seems quite ad-hoc. Though it's not a prompt-based method, but it's trying to distill the prompt-based method into a low-rank representation space. From this perspective, it's still a prompt-based approach. 
2. The prompt-based approach has many mentioned limitations. Also, it's really hard to make sure the content is exactly the same while only the style gets shifted. This error in the data synthesis pipeline will influence the performance of the method.
3. The experiments of this paper is highly limited to two styles. These two styles can be easily achievable by prompting. The paper was motivated to go beyond this, however, the experiments do not support that.

### Questions
The notation in section 4 is quite confusing. 

1. I don't see the definition of N in equation (4). The lowercased n seems to indicate the dataset size. But the capital N seems to indicate a different thing?
2. the q_i in SVD shares the same notation as equation (3). But I think they are totally different things.
3. why is q missing in equation (5)? There isn't enough justification for that.

### Soundness
3

### Presentation
3

### Contribution
2
