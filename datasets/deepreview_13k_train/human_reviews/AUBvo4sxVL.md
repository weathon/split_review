# MatExpert: Decomposing Materials Discovery By Mimicking Human Experts

- Decision: Accept
- Scores: 6, 6, 6, 6

## Abstract
Material discovery is a critical research area with profound implications for various industries. In this work, we introduce \textit{MatExpert}, a novel framework that leverages Large Language Models (LLMs) and contrastive learning to accelerate the discovery and design of new solid-state materials. Inspired by the workflow of human materials design experts, our approach integrates three key stages: retrieval, transition, and generation. First, in the retrieval stage, MatExpert identifies an existing material that closely matches the desired criteria. Second, in the transition stage, MatExpert outlines the necessary modifications to transform this material formulation to meet specific requirements outlined by the initial user query. Third, in the generation state, MatExpert performs detailed computations and structural generation to create new materials based on the provided information. Our experimental results demonstrate that MatExpert outperforms state-of-the-art methods in material generation tasks, achieving superior performance across various metrics including validity, distribution, and stability. As such, MatExpert represents a meaningful advancement in computational material discovery using langauge-based generative models.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
MatExpert is designed to streamline the discovery of new materials using LLMs and contrastive learning. Inspired by the traditional workflow of human experts, MatExpert operates in three stages: retrieval, transition, and generation. Experimental results demonstrate that MatExpert outperforms current sota models in material generation tasks.

### Strengths
1. The design of MatExpert mirrors the expert-driven process in material science, breaking down material generation into retrieval, transition, and generation stages. This structured approach allows for iterative refinement.

2. The transition stage uses a CoT reasoning process, enabling the model to outline logical, step-by-step modifications to meet target properties. This sequential reasoning contributes to the model's ability to achieve high accuracy in conditional generation tasks.

3. By compiling a dataset of over 2 million materials from NOMAD, MatExpert provides a large-scale testbed to assess its performance.

### Weaknesses
1. While the multi-stage design of MatExpert improves accuracy, it adds computational complexity and potentially increases training time compared to single-step models. 

2. The proposed framework will have cumulative errors. If the result retrieved in the first step is far away from the target, it will be difficult to correct it later, thus affecting the results of subsequent steps.

3. This paper focuses on innovation in application scenarios, and the technological innovation is relatively limited.

### Questions
The heavy reliance on specific material databases, such as NOMAD, might lead to overfitting or model bias toward these datasets. Testing MatExpert on unseen data sources or a wider array of material properties could offer better insights into its generalization capabilities.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper describes a novel LLM based framework for materials discovery (MatExpert). There are three stages to the MatExpert methodology: retrieval, transition, and generation. First, a material is retrieved from the database that most closely matches the description given (similarly was trained with contrastive learning). Next during transition, the model determines how to alter the retrieved material to match the desired properties. Lastly, in the generation phase the model produces a ALX representation that is converted into a CIF representation. The main contribution of the paper is the MatExpert framework and the accompanying benchmarking and ablation study.

### Strengths
- The application of LLM to materials is interesting and materials discovery is important
- The evaluation metrics includes stability computed with DFT not just proxy metrics 
- Writing style and related work are good

### Weaknesses
 - Lacking details on what data was used for which tasks? For the unconditional results on MP-20, it is unclear if the NOMAD data was also used for training MatExpert. For the conditional results, were CrystalLLM and MatExpert trained on the same data?
- The results in Figure 5 are not well quantified i.e. it is not clear MatExpert is better. Also, there are 11 bars but only 9 labels, not sure if I missed something? The colors are very similar in some cases, hard to parse quickly.   
- There is no discussion on the limitations of using the retrieval stage. My interpretation is that the retrieved material is like a template. Before generative models, new materials were searched for using templating/substitution methods. One of the critiques of those methods is that materials generated are still quite similar to the template, would that also be a limitation here?

### Questions
- The paper mentions that the wdist density and wdist number of elements metrics are greatly improved compared to CrystalLLM but if the model is given a template from the database does that undermine these metrics? Is there a way to test this? For example, how often does the generated structure change the number of elements compared to the retrieved/given material? 
- Can you compute the S.U.N metric from Zeni et al. (https://arxiv.org/abs/2312.03687)?
- How does the inference speed of MatExpert compare to CrystalLLM?

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper presents MatExpert, a framework that leverages large language models (LLMs) and contrastive learning to automate materials discovery. The proposed approach mimics human experts by breaking the process into three stages: retrieval, transition, and generation. MatExpert first identifies a closely related material, then suggests modifications to meet target specifications, and finally generates new material structures. The authors test MatExpert with large datasets from NOMAD and the Materials Project, showing that it performs better than current methods on key measures like stability, validity, and how well it meets diversity and novelty.

### Strengths
* The integration of Robocrystallographer enriches crystal data with textual descriptions, enhancing the retrieval process and interpretability.
* MatExpert achieves impressive performance on benchmarks, demonstrating its reliability in generating valid and diverse material structures.
* Contrastive learning effectively maps structure and property embeddings, which is a novel approach for aligning multimodal material data.

### Weaknesses
 * The novelty of multi-stages material generation is a bit limited as it’s being studied in other works [1, 2, 3].  In the introduction, the author mention the drawback of the current method is the single step material structure generation. However, some cited paper include multi-steps material generation and property query already [1, 2, 3]. It will be helpful to have more discussion on those methods.
* The paper could benefit from more clarity on the pathway generation process. Specifically, it is unclear how the pathways generated by GPT-4 can be reliably reproduced in real-world lab settings. The authors might find [4] useful as a reference for evaluating the quality and safety of generated pathways.
* Due to the complexity of multi-steps framework, the paper could discuss more on how the authors prevent the error propagation.
* The visualization for Figure 6 is not clear enough. If there’s a table include the numerical value of the ablation study, it can better show the improvement of each component.
* The design choice of structure retrieval over natural language processing (NLP) corpora is not sufficiently justified. It's unclear why chemical structures offer a significant advantage over textual data, which inherently provides richer contextual information. The paper needs to clarify if chemical structures provide a more compact representation without losing the information conveyed in textual descriptions.
* The novelty of the chain-of-thought (CoT) approach is incremental, given the demonstrated improvements of CoT in prior works. The paper should elaborate on how the CoT reasoning applied here diverges from or expands upon existing methods, rather than simply applying a standard CoT approach.

### Questions
* Follow up on W1, given the reproducibility challenges in LLM-generated content, how does the framework handle multiple potential pathways for synthesizing a target material?
* Follow up on W3, I wonder what’s MatExpert’s the success rate on each step? Specifically, the success rate for generating accurate ALX representation.
* Can this method be useful for user query without specifying formation energy and band gap for the target material? For instance, can the user prompt the model like, I want to material composed of Mn, Ge and with high electrical conductivity.
* What will the model response if the target material doesn’t exist?

[1] Miret, Santiago, et al. “Are LLMs Ready for Real-World Materials Discovery?”

[2] Zhang, Huan, et al. “HoneyComb: A Flexible LLM-Based Agent System for Materials Science”

[3] Chiang, Yuan, et al. “LLaMP: Large Language Model Made Powerful for High-fidelity Materials Knowledge Retrieval and Distillation”

[4] Microsoft Research AI4Science. “The Impact of Large Language Models on Scientific Discovery: a Preliminary Study using GPT-4”

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper proposes MatExpert framework, designed to enhance LLM-based crystal structure generation through a 3-stage inference. The first stage searches an existing structure that closely resembles the user's input via T5 model trained with a contrastive learning objective on property and structure descriptions. Then, the fine-tuned LLM suggests modifications to the physical properties and structural attributes to achieve the target composition and characteristics. Finally, the LLM generates an ALX representation, which is converted to the final crystal structure. The authors also introduce a curated, large-scale dataset for training and demonstrate that this iterative, feedback-driven approach improves all evaluation metrics.

### Strengths
1. This paper presents a novel approach by modeling crystal structures with a chain-of-experts framework that utilizes multiple LLMs. As far as I know, this approach is novel, and appears effective in generating stable materials.
2. Additionally, the use of fine-tuning methods, such as LoRA and distillation, enhances the framework’s efficiency and scalability, making it practical for real-world adaptation.

### Weaknesses
1. The authors mentioned in the paper that “In the unconditional generation task, we aim to assess the ability of MatExpert to produce novel and stable material structures without any specific property constraints”, while at the same time “... For unconditional generation, we randomly select a material from the database during the first stage of MatExpert.” According to the second referred sentence, the second, transition stage would take samples of training set embeddings or raw data would be given as input. This is contradictory to the claim that no structure or property is given to generate. For this reason, I believe the evaluation scheme is unfair. Please fix me in the author response if I understood incorrectly.

2.  Following this concern, the performance improvement on generation is also questionable. The authors are encouraged to provide stabilities (Predicted energy over convex hull values, or DFT relaxation success rate) of the generated samples that are out-of-distribution. Also, stability measurements on Table 2 are also needed.

3. There are stronger baselines following the CDVAE research, as the authors stated. However, comparisons between them, which is necessary, are missing in Table 1.  Furthermore, the authors also need to specify which dataset was used, or, the source of the CDVAE model. If the CDVAE model is trained only on MP-20, that would not be a fair comparison.

### Questions
1. In Figure 5, are all the structures relaxed or not? Does it contain all generated samples, or samples that passed the validity test? Please provide the details.

2. Have you checked the energy value difference between the model inputs and generated samples? If there are OOD samples, does it pass the validity test or relaxation steps?

3. Regarding Equation (1), what do you use as the similarity function?

4. What prompts have you given to the model? Concretely, how much overlap is there between the conditioned properties and the NOMAD data?

### Soundness
2

### Presentation
2

### Contribution
2
