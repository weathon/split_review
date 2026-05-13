# Reasoning Limitations of  Multimodal Large Language Models. A case study of Bongard Problems

- Decision: Reject
- Scores: 5, 3, 3, 8

## Abstract
Abstract visual reasoning (AVR) encompasses a suite of tasks whose solving requires the ability to discover common concepts underlying the set of pictures through an analogy-making process, similarly to human IQ tests.
Bongard Problems (BPs), proposed in 1968, constitute a fundamental challenge in this domain mainly due to their requirement to combine visual reasoning and verbal description.
This work poses a question whether multimodal large language models (MLLMs) inherently designed to combine vision and language are capable of tackling BPs.
To this end, we propose a set of diverse MLLM-suited strategies to tackle BPs and examine four popular proprietary MLLMs: GPT-4o, GPT-4 Turbo, Gemini 1.5 Pro, and Claude 3.5 Sonnet, and four open models: InternVL2-8B, LLaVa-1.6 Mistral-7B, Phi-3.5-Vision, and Pixtral 12B.
The above MLLMs are compared on three BP datasets: a set of original BP instances relying on synthetic, geometry-based images and two recent datasets based on real-world images, i.e., Bongard-HOI and Bongard-OpenWorld.
The experiments reveal significant limitations of MLLMs in solving BPs.
In particular, the models struggle to solve the classical set of synthetic BPs, despite their visual simplicity.
Though their performance ameliorates on real-world concepts expressed in Bongard-HOI and Bongard-OpenWorld, the models still have difficulty in utilizing new information to improve their predictions, as well as utilizing a dialog context window effectively.
To capture the reasons of performance discrepancy between synthetic and real-world AVR domains, we propose Bongard-RWR, a new BP dataset consisting of real-world images that translates concepts from hand-crafted synthetic BPs to real-world concepts.
The MLLMs' results on Bongard-RWR suggest that their poor performance on classical BPs is not due to domain specificity but rather reflects their general AVR limitations.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper focuses on the capability of multimodal large language models (MLLM) to solve Bongard Problems (BP). The authors propose a new BP dataset, where the two sides of the images are distinguished by abstract visual concepts. The authors design a set of evaluation methods for MLLMs, including binary classifications and solving BP using different generation strategies. The results on the proposed BP dataset and three other BP datasets show that the abstract visual reasoning capabilities of MLLMs are limited in solving BP, especially in the proposed ones.

### Strengths
The paper provides a comprehensive evaluation of the capabilities of vision language models on Bongard Problems (BPs). The paper includes eight models and 10 metrics to evaluate them on 4 types of BPs, including one created by the authors. I believe it will be very helpful for future study of BPs.

### Weaknesses
 - The presentation of the paper needs to be improved. Despite numerous settings, new generation strategies and new dataset, the authors choose to present the results in just one table. It is almost impossible to interpret the table and verify the claims made by the authors without checking back and forth. I suggest reviewer break down the table into small ones, where each of them provides a clear message to the readers. If that takes more space than the current version, some of the experiment results can be moved to appendix.
- The observation from the results is currently not very interesting. The major claim made by the authors is that the capability of the VLMs on BPs are limited. Not many intuitions behind are obtained, part of it is because of the poor presentation, and the other part is probably because the observations are not very consistent across different models. I suggest the authors dive deep into the details and conduct additional experiments if necessary. Overall, I believe the contribution of the paper can be improved.
- The new BP dataset created in the paper is quite difficult for the models. I believe a comprehensive human study is necessary in this case to ensure the validity of the dataset. It is great that the dataset is released, but after a quick scan of the dataset, I personally find it very hard to distinguish the left and the right images for some BPs. Therefore, I suggest the authors to report human performance on the tasks and report consistency across human annotators.

### Questions
It would be nice to show some human score for BPs. Is there any attempt toward that?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper focuses on exploring one limitation of MLLM in visual understanding: there is still a big gap between MLLMs and humans in the IQ test / AVR test from psychometrics. They choose Bongard Problems to conduct the case study. Firstly, they build a new benchmark with some Bongard Problem samples. Then, they compare some SOTA MLLMs and VLMs with this multi-image reasoning task. The results suggest that the weak performance of MLLMs on Bongard Problems is not due to the domain specificity, but rather comes from their multi-image reasoning capability.

### Strengths
1. This is an important problem for MLLM nowadays. I like the motivation of your paper. As we know, Human IQ test has a long history in psychometrics and only a few of works try to explore the different between MLLM and human in this topic [1].    

2. They have open-sourced their dataset containing 100 samples. I have a quick review of the dataset repo. The data structures and descriptions are easy to follow.  

3. Compare with most of visual reasoning benchmark papers, this paper use less data but it has a solid cognition background. I happen to agree with some viewpoints of the authors, which are also highlighted by Google DeepMind recently.      

References:     
[1] Galatzer-Levy, Isaac R., et al. "The Cognitive Capabilities of Generative AI: A Comparative Analysis with Human Benchmarks." arXiv preprint arXiv:2410.07391 (2024).

### Weaknesses
1. It is worth to highlight that BP is only a subtask of AVR test. Compared to RAVEN, BP is not widely used by human's IQ test recently. I think you should discuss this limitation and consider exploring a board scope of AVR tasks in the future work.

2. The Evaluation settings in Figure 3 is unclear. It seems that most of the settings proposed by you can only use to test the closed-sourced models like Claude 3.5 and GPT-4o. The multi-image reasoning capbility of most of open-sourced MLLMs are not eligible in these tasks.

3. For a better understanding, the user study between human and MLLM is also important for this task.

4. Lacking an in-detailed analysis of the 100 samples in your datatset, e.g. the difficulty of each image pair.

5. The data selection process for your dataset remains unclear. The GPT-4o data generation process involves manual intervention at several steps. This raises concerns about how these manually selected images align with the design standards of Bongard problems. A potential risk is that readers might question whether your dataset was manually selected to emphasize the weaknesses of MLLMs, particularly in terms of the data are sampling from conditional probability distributions. This could contradict the foundational principles of Bongard problems and potentially undermine the validity of your conclusions.

### Questions
1. What is your insight on these proposed generation strategies in Figure 2? (Why do you choose these tasks?)

2. There are also some works from the observation in psychological experiments like MindSet [1], which could be the data sources for BP tasks or AVR tasks.

3. As your works show some similar observations to previous benchmark works like VCog-Bench, and François Chollet's book "On the measure of intelligence, you can put some further discussions in the main body of your paper.

Post Rebuttal:

I take a quick view of the authors' reply and other reviews' score, I decide to decrease my final score to 4. Though the authors choose a good topic for motivation, the main pain points (over claiming, lacking data, lacking detailed definition) are difficult to solve. This, we all agree this paper doesn't match the bar of ICLR.

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper investigates the Bongard Problems (BPs) as a case study in Multimodal LLMs. This problem represents a foundational problem in Abstract visual reasoning (AVR). This paper gathered a new dataset Bongard-RWR and used multiple strategies to test the proprietary and open-sourced MLLMs on both synthetic and real-world BPs. The experiments show that there is still a gap for MLLMs to do AVR, but certain strategies.

### Strengths
1. The problem of Abstract visual reasoning (AVR) is a popular problem and has gained great attention lately. The perspective of Bongard Problems is novel and meaningful.
2. The experiments of this paper are comprehensive on various MLLMs and 4 datasets (one of them is newly collected by this paper).
3. The dataset is already open-sourced, which may contribute to the research community in the future.

### Weaknesses
1. The contribution of the proposed Bongard-RWR dataset is not clear enough, although the authors briefly mentioned in Line 311-312. The previous datasets already covered both synthetic and real-world settings. How do the proposed datasets differentiate from these datasets? It is unclear why the authors find previous datasets insufficient or lacking in meaningfulness due to differences in concepts.
2. While the paper evaluates current MLLMs, it fails to offer a clear direction for enhancing their AVR capabilities or to present any new insights beyond highlighting general limitations. The results of different strategies might only reflect the training data (instruction tuning data) for these models. 
3. Since the newly gathered dataset is considered as a main contribution, there are no clear statistics of this dataset provided. The lack of detailed statistics, such as the distribution of concepts, the complexity of the visual patterns, and the inter-annotator agreement during the dataset creation, makes it difficult to assess the dataset's quality and its suitability for evaluating abstract visual reasoning. Furthermore, the sample size of 100 raises methodological concerns. Given the potential for various sources of bias, this limited sample may not provide sufficient statistical power to draw robust conclusions.

### Questions
- Can you provide the rationale behind the proposed strategies in the experiments? Does it relate to the theory of AVR from a cognitive science perspective? Can you summarize the high-level idea of the design?
- To further understand the limitations, do you think the same model with different sizes (LLaVA 1.6 7b/13b/70b) will highlight some observations? I think it can reveal how scaling law will help with this problem.
- Can you list the key reasons why MLLMs fail in BPs? This should be provided in the conclusion section. You need to expand "broader limitations in their reasoning abilities" in Line 537-538.

### Soundness
2

### Presentation
3

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
This paper investigates the abstract reasoning capabilities of multimodal large language models (MLLMs) using Bongard Problems (BPs), which require analogy-making between sets of images. The authors test several MLLMs on both synthetic and real-world BP datasets, highlighting significant limitations in their performance, especially with abstract, synthetic problems. Despite some improvement with real-world images, the models still struggle with effectively incorporating new information and handling complex visual reasoning tasks. To address this, the paper introduces a new dataset, Bongard-RWR, translating synthetic BP concepts into real-world images.

### Strengths
- The paper studies an interesting topic of Bongard Problems (BPs). It introduces a comprehensive evaluation of MLLMs using BPs, which are notoriously challenging in abstract reasoning. By testing both synthetic and real-world BP datasets, the authors highlight critical weaknesses in these models, providing valuable insight into their current capabilities. This positions BPs as a powerful benchmark for future MLLM advancements.
- This paper creates Bongard-RWR to bridge the gap between abstract synthetic reasoning and real-world tasks. This dataset allows for more meaningful comparisons of MLLM capabilities across domains. Also, this dataset enables future work to pinpoint the source of reasoning failures more precisely.
- The paper is well written and easy to understand.

### Weaknesses
I didn't see major weaknesses.

### Questions
- Some open-source models like InternVL2 and Phi-3.5V perform well on many benchmarks but struggle, nearing chance-level performance on Bongard Problems, while LLava-1.6 and Pixtral perform okay. What do the authors think causes these discrepancies?
- How closely does abstract visual reasoning (AVR) reflect real-world visual reasoning (VR)? For instance, if a model excels in AVR, can we expect it to perform well in VR, and vice versa? Some potential correlations experiments between AVR and VR performance might give some insights.

### Soundness
3

### Presentation
3

### Contribution
3
