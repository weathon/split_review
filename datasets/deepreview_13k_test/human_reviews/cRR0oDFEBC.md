# Self-play with Execution Feedback: Improving Instruction-following Capabilities of Large Language Models

- Decision: Accept
- Scores: 6, 8, 8, 8, 6

## Abstract
One core capability of large language models~(LLMs) is to follow natural language instructions. 
However, the issue of automatically constructing high-quality training data to enhance the complex instruction-following abilities of LLMs without manual annotation remains unresolved. 
In this paper, we introduce \modelname, the first scalable and reliable method for automatically generating instruction-following training data. 
\modelname transforms the validation of instruction-following data quality into code verification, requiring LLMs to generate instructions, the corresponding code to check the correctness of the instruction responses, and unit test samples to verify the code's correctness.
Then, execution feedback-based rejection sampling can generate data for Supervised Fine-Tuning (SFT) and Reinforcement Learning from Human Feedback (RLHF) training.
\modelname achieves significant improvements across three training algorithms, SFT, Offline DPO, and Online DPO, when applied to the top open-source LLMs, Qwen2 and LLaMA3, in self-alignment and strong-to-weak distillation settings.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This work presents AUTOIF, a generic and automated framework for the generation of high-quality training data to enhance the instruction-following prowess of LLMs. The main novelty of this work is that it reduces instruction-following alignment to a verifiable process using code. AUTOIF leverages execution feedback from code verification and rejection sampling to guarantee that the generated responses meet given constraints. This technique has paved the way for preparing both positive and negative examples for algorithms using SFT and RLHF. The authors mention that AUTOIF substantially improves the performance of LLMs on many benchmarks without weakening other competencies, such as coding and mathematical reasoning.

Besides this, the paper presents an extensive experiment to show that AUTOIF improves the instruction-following accuracy of a range of LLM architectures and sizes, from Qwen2 and LLaMA3 models. The paper underlines that indeed one of the keys to good performance is iterative online training and at the same time develops the scalability and generalization potential of AUTOIF across diverse types of instructions.

### Strengths
Extensive Performance Improvements: AUTOIF leads to significant gains across various instruction-following benchmarks, such as IFEval and FollowBench. It notably achieves over 90% loose instruction accuracy on IFEval while preserving or even slightly improving performance on other key capabilities like coding and mathematical reasoning.

Comprehensive Evaluation and Ablation Studies: The research includes a thorough evaluation of AUTOIF across different models, parameter sizes, and ablation settings, demonstrating the robustness and scalability of the approach. It also explores data scaling and efficiency, highlighting the method's potential to achieve strong performance with relatively fewer data samples.

Balanced Capability Improvement: AUTOIF enhances instruction-following without compromising other model abilities, such as coding and general reasoning, making it a well-rounded solution.

### Weaknesses
Conceptual Rigidity: While the core contribution of this paper is insightful, the attempt to cast the instruction-following alignment into a code verification problem introduces some rigidity. This is so because in that respect, focus will be on "verifiable instructions" that can be amenable to mechanical verification by code executors. While the structure for this argument is robust in this text, it might indeed be narrow to encompass more complex or subjective tasks. The paper does not delve into the non-code-based verification methods like model-based scoring or human-in-the-loop strategies; the thrust of the discussion remains centered on the execution feedback mechanism​.

Generalization Concerns: Concentration on verifiable instructions has been made amply clear in the method section. AUTOIF framework uses code for instruction verification, which in itself inherently limits the generalization to open-ended or subjective instructions. While the paper does highlight improvements across benchmarks such as IFEval, it does not really investigate how the approach generalizes when the tasks are less structured or ambiguous. Though the second concern with respect to AUTOIF biasing the models to easily verifiable instructions might be well-taken, given the current evidence, it should be framed as a hypothesis.

Somewhat worrying lack of methodological diversity: there is heavy focus on execution feedback. Other methods are not considered, like human feedback or model-based evaluation. Still, the paper does state that execution feedback and iterative optimization work fine, so there is a possibility that with more methods added, the instruction-following capabilities could be further improved.

It is very clear that, when explaining the strengths of the method, it seems over-dependent on automation and slighting the benefits that could be derived from purposive human intervention. The consideration of benefits from a more balanced approach in complex situations is thus little. By allowing human insights to complement this framework, therefore, it would adapt to inclusivity in the given context.

Novelty: Automatic instruction verification might not be an entirely new idea. Works in this area are CodeLlama2, PLUM, LLaMA3, SelfCodeAlign, and DeepSeek-Coder-V2. In fact, research efforts such as code-based execution feedback and automated instruction alignment have been made. For example, CodeLlama2 and LLaMA3 utilized the base of code-based synthesis and validation frameworks in their architectures for better performance on top of instruction-following tasks, which underlines code execution as a natural source of feedback. Simultaneously, these related works suggest that perhaps AUTOIF, with the novelty of scalability and data synthesis, is not really a new fundamental direction in the space.

### Questions
How could the framework be extended to manage instructions that are inherently ambiguous or have multiple valid responses?

What modifications to AUTOIF would be necessary to accommodate tasks involving emotional nuance or creative outputs?

Could providing more detailed information on errors and failure rates improve the replicability and robustness of AUTOIF?

What specific criteria were used to filter low-quality instructions, and can this process be made more transparent?

What are the computational overhead implications of using execution feedback at scale, and are there any optimizations or trade-offs that can be explored?

How does AUTOIF perform in resource-constrained environments, and is there a way to quantify these trade-offs more concretely?

### Soundness
3

### Presentation
4

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper presents AutoIF. The main idea of AutoIF is to generate constraint-following instruction data by generating validation functions that correspond to the constraints within the natural language instruction and running them to validate any prospective responses.

### Strengths
- This paper looks at an important problem of training LLMs to precisely follow instructions
- The proposed approach is novel and seems general to most scenarios. It can be used to improve the quality of instruction-following datasets.
- This paper comes with comprehensive end-to-end evaluations as well as controlled experiments, with good insights and reasonable explanations.

### Weaknesses
- Section 3.2: cross-verification can be weak as it essentially assumes test-function self-consistency as correctness. Not sure how reliable is self-consistency here as (i) bad tests can kill the right function and (ii) tests and functions can be broken all together result in corrupted data quality. 

----

Other minor suggestions:

- Code execution has also been widely adopted in the code domain to generate test-assured code; it is generally good to discuss more of such work (not only just CodeRL; but also RLTF, LEVER, Self-OSS-Instruct, ODEX, etc.) to connect the general research context.
- L209: It might be more accurate to cite the use of rejection sampling with "Training a helpful and harmless assistant with reinforcement learning from human feedback" in addition to/instead of the Llama 2 paper.
- L210: what does "_{j=1}" mean? Do you mean "i=1"?

### Questions
- I am curious about counter-examples where programs cannot model the constraints in the instruction; and how to recognize such cases and delegate them to human experts.
- Section 3.2: How reliable is cross-validation of test cases and verification functions? Do you see cases where cross-consistent test and verifiers are wrong together?

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
The paper proposes AutoIF, a scalable method for generating high-quality instruction-following data for training LLMs without manual annotation. It leverages code execution to verify response quality. LLMs are used to generate instructions, produce the corresponding code, and create unit test samples for cross-validation. Execution-based rejection sampling produces data for SFT and RLHF. Applied to Qwen2 and Llama3, AutoIF enhances performance across three training algorithms (SFT, offline DPO, online DPO), achieving over 90% accuracy in IFEval’s loose instruction accuracy benchmark without sacrificing general, math, or coding abilities, highlighting its effectiveness in alignment and generalization.

### Strengths
1. The technique is intuitive. IFEval was constructed using verifiable instructions to test an LLM's instruction-following ability, while this paper generates verifiable code to evaluate the instruction-response alignment.
2. AutoIF proves to be effective in the self-alignment case, where the same model is used for instruction generation and verification.
3. The evaluation covers a wide range of benchmarks and shows that AutoIF improves instruction following significantly while preserving the other general capabilities.
4. AutoIF naturally generates pair-wise preference data and can be applied to DPO, offline or online.

### Weaknesses
1. In the self-alignment setting, the evaluation is only conducted on the two >70B models. It is unclear whether the same conclusion applies to weaker base models with less than 10B parameters.
2. There are strong-to-weak and self-alignment settings, so a weak-to-strong setting should logically be included. There’s no proper justification for leaving it out.
3. There's a missing baseline where responses are validated through the LLM itself without code. Without the baseline, it's unclear how valuable the verification function and test cases are.

### Questions
1. See the weaknesses above.
2. Line 107: `we validate AUTOIF’s effectiveness in both "Self Alignment" and "Weak to Strong"`. typo?
3. Will the self-alignment setting still work for smaller models like Llama3-8B?
4. What are the main technical differences from StarCoder2-Instruct, which also used the base model itself to generate instructions, code, and test cases for validation?
5. Although the IFEval and FollowBench results are impressive, these benchmarks are specifically designed to test natural language instruction following. Can improved IFEval performance be linked to more practical tasks? For instance, while benchmarks like GSM8K and HumanEval may not show additional gains, BigCodeBench / LiveCodeBench / LeetCode include complex instruction-following cases, which should ideally lead to improvement.
6. Are there analyses on how reliable the generated code and tests are? Either or both of them may be just wrong.

If my concerns are properly addressed, I will consider raising the score.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper proposes AUTOIF, an automated, scalable, and reliable method designed to enhance the instruction-following capabilities of LLMs, using automatic code verification.

### Strengths
There is a detailed and structured pipeline of AutoIF which showcases enhanced results over multiple training strategy.

### Weaknesses
However, examples on failed cases and illustration of these categories of consistent failure would help understand scope of next steps and areas of improvement that has been brought about by the method. Along with the limited domain of seed instructions in terms of string manipulation only, which could be diversified.

### Questions
- Figure 2, improve consistency of terms in figure with 'acc' and 'Acc' being used alternatively, and the sequence of verification and func set being inverted at start.
- An example case of how a sample develops in the AutoIF pipeline would help illustrate the working even better. 
- Line 215, 232, provide reasoning and example of failing cases of why accuracy is lower. similarly for Section 4.1 talks about main results but is limited to quantitative numbers and not examples of illustrating failed cases.
- Also, most seed instruction showcase restriction over string manipulation domain only. Ensuring type of word to be present, limiting length of output and so on. There is no showcasing of diverse, novel instructions. 
- line 319, what is the value of K, for which the results have been sampled from?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The authors propose AUTOIF, a training framework to improve instruction following capability via execution feedback. The authors demonstrate the efficacy of AUTOIF on four LLMs with benchmarks across various domains.

### Strengths
There are a few valuable contributions:
- The proposed AUTOIF shows that training with program-based validation can improve some instruction-following capabilities.
- The experiments are pretty extensive, where the authors benchmark the AUTOIF on four models with different sizes.
- The ablation studies are quite detailed, showing the optimal setups for AUTOIF.

### Weaknesses
There are several weaknesses to be addressed:
- The idea of using programs to validate instruction-following is not novel, as it has been used in IFEval. Moreover, training with execution feedback is also not new; it has been widely used by training code LLMs [1-3].
- Based on the proposed workflow, AUTOIF is hard to scale to complex instructions, where the queries are totally quantifiable. AUTOIF cannot easily work for semantically rich instructions, which cannot be evaluated via execution. In addition, real-world scenarios that can be validated via programs may require various dependencies and APIs. AUTOIF is not scalable under these practical cases. 
- The instruction-following evaluations on IFBench and FollowBench lack practicability. These two benchmarks only contain quantifiable instructions, like word counts. The authors should consider more practical scenarios like the one in BigCodeBench [4] for the instruction-following evaluation.
- The current evaluation is English-only. The authors should evaluate their models on multilingual setups to demonstrate their generalisability.

[1] Le, H., Wang, Y., Gotmare, A. D., Savarese, S., & Hoi, S. C. H. (2022). Coderl: Mastering code generation through pretrained models and deep reinforcement learning. Advances in Neural Information Processing Systems, 35, 21314-21328.

[2] Zheng, T., Zhang, G., Shen, T., Liu, X., Lin, B. Y., Fu, J., ... & Yue, X. (2024). Opencodeinterpreter: Integrating code generation with execution and refinement. arXiv preprint arXiv:2402.14658.

[3] Chen, B., Zhang, F., Nguyen, A., Zan, D., Lin, Z., Lou, J. G., & Chen, W. CodeT: Code Generation with Generated Tests. In The Eleventh International Conference on Learning Representations.

[4] Zhuo, T. Y., Vu, M. C., Chim, J., Hu, H., Yu, W., Widyasari, R., ... & Von Werra, L. (2024). Bigcodebench: Benchmarking code generation with diverse function calls and complex instructions. arXiv preprint arXiv:2406.15877.

### Questions
Apart from the mentioned weaknesses, there are some additional questions:
- How do the accuracy rate thresholds in the verification steps affect the model performance?
- How does RAILF+Online DPO (e.g., OAIF [1]) compare to AUTOIF?

[1] Guo, S., Zhang, B., Liu, T., Liu, T., Khalman, M., Llinares, F., ... & Blondel, M. (2024). Direct language model alignment from online ai feedback. arXiv preprint arXiv:2402.04792.

### Soundness
3

### Presentation
3

### Contribution
2
