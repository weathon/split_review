# Understanding Jailbreak Success: A Study of Latent Space Dynamics in Large Language Models

- Decision: Reject
- Scores: 5, 3, 5, 6

## Abstract
Conversational large language models are trained to refuse to answer harmful questions. However, emergent jailbreaking techniques can still elicit unsafe outputs, presenting an ongoing challenge for model alignment. To better understand how different jailbreak types circumvent safeguards, this paper analyses model activations on different jailbreak inputs. We find that it is possible to extract a  \textit{jailbreak vector} from a single class of jailbreaks that works to mitigate jailbreak effectiveness from other semantically-dissimilar classes. This may indicate that different kinds of effective jailbreaks operate via a similar internal mechanism. We investigate a potential common mechanism of harmfulness feature suppression, and find evidence that effective jailbreaks noticeably reduce a model's perception of prompt harmfulness. %provide evidence for its existence at the end of harmful prompts with a jailbreak. 
These findings offer actionable insights for developing more robust jailbreak countermeasures and lay the groundwork for a deeper, mechanistic understanding of jailbreak dynamics in language models. \textbf{Disclaimer: This paper includes disturbing language in some examples.}

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper explores how jailbreaking techniques work by analyzing latent space dynamics in large language models. The authors found that different types of jailbreaks might share a common internal mechanism and that a jailbreak vector from one class can mitigate others, and that effective jailbreaks can reduce the model's perception of prompt harmfulness. These findings provide valuable insights for understanding jailbreaks and developing better safeguards in large language models.

### Strengths
* This paper provides a new perspective to understand jailbreak by analyzing latent space dynamics in large language models. Their findings are very interesting that different types of jailbreaks might share a common internal mechanism and a jailbreak vector can be used to improve/reduce safety of large language models.
* The paper covers many different kinds of jailbreak methods, making it more convincing that there may exist a common internal mechanism in large language jailbreaking.

### Weaknesses
 * This paper only evaluate 4 models and some of them are not well aligned, e.g. Vicuna is only trained on ShareGPT dataset without RLHF/DPO Stage. In addition, these four models do not behave consistently, e.g. Vicuna shows better cluster patterns than Qwen 14B Chat. In addition, from Vicuna 7B to 13B, I also find that 13B model activation cluster is scattered. This made me question that when the model goes to large sizes and more aligned, will these patterns be less obvious and visible? Hence, I think the authors may compare more aligned models like Llama 3.1 in various sizes and study if they follow similar patterns.

* The authors study how to use the  jailbreak vector to reduce/improve jailbreak success. My question is that in practice, how do we use such techniques? If we minus jailbreak vectors for both harmful and harmless questions, will it reduce the models' helpfulness/correctness/truthfulness? It will be interesting to know these results in general benchmarks like MMLU or AlpacaEval.

### Questions
See comments in Weaknesses.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper investigates how different types of jailbreaks in LLMs might share underlying mechanisms, making it possible to counter multiple jailbreaks using shared “jailbreak vectors.” The study finds that effective jailbreaks tend to reduce a model’s perception of harmfulness, suggesting a way to develop more resilient safeguards against these manipulations.

### Strengths
Strengths
1.	Some new Insights on Jailbreaks: the paper explores how different jailbreak types in LLMs might share common mechanics, providing a relatively fresh view on understanding and countering them.
2.	Possible Mitigation Solution: By identifying shared jailbreak properties, the study suggests ways to create more robust defenses against jailbreak attacks.

### Weaknesses
Weaknesses
1.	Limited Model Range: The study focuses on only a few models, which may make its conclusions less generalizable. Moreover, the choice of Vicuna lacks sufficient justification, as it may not adequately represent the current SOTA among 7B/13B models. The lack of diversity in model architectures and training methodologies limits the scope of the findings. For example, models trained with different loss functions or on different datasets might exhibit different responses to the jailbreak vectors. The study should include a more diverse set of models, including those with different alignment techniques, to ensure the robustness of the conclusions.
2.	Related work is not highly related to the research topic of this paper and did not include the most recent studies on understanding the how jailbreak works in the LLMs. The related work section should include more recent studies that explore the mechanisms of jailbreaks, such as those focusing on adversarial perturbations in the embedding space or the role of specific layers in processing harmful requests. The current related work section does not adequately contextualize the study within the broader field of LLM security research.

### Questions
The authors said "layer 16 for 7B and layer 20 for 13B and 14B parameter models" in line 162, my question is "Multiple layers, rather than a single layer, should be considered as the middle layers. what if we select a different middle layer, e.g., layer 14 for 7B, layer 24 for 13B. will this have some influences on the results?"

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper aims to understand existing jailbreak methods over LLMs by analyzing the latent space dynamics. First, they constructed jailbreak vectors based on the activations of LLMs calculated on harmful datasets and harmless datasets. They find that the jailbreak vector from a single class of jailbreaks can also work to mitigate jailbreak effectiveness from other semantically-dissimilar classes. Second, they analyze the evolution of cosine similarity between harmfulness direction and activations at each token position for one harmful question without jailbreak (none) and for different jailbreak types. They find that successful jailbreaks have significantly lower representations of harmfulness at the end of instruction for most models, which indicates that the jailbreaks suppress the harmfulness feature on the prompts.

### Strengths
1.	It is interesting to use jailbreak vectors for analysis. The paper also demonstrated that jailbreak vectors can  effectively prevent the success of jailbreaks across different types via activation steering, pointing to a shared underlying mechanism.

2.	The paper discussed the concept of models’ perception of prompt harmfulness, and suggested that some jailbreaks succeed by reducing the perception of prompt harmfulness, preventing the refusal response.

### Weaknesses
1. The presentation of methodology part can be improved by providing a workflow figure. This can help people better understand how and where the jailbreak vectors are calculated, and also how the mitigation is performed. 

2. The findings in Section 5.2 need to be re-evaluated carefully. They find that jailbreak steering vectors have a positive cosine similarity with one another, and hypothesize that jailbreak vectors from one class will work to steer away from successful jailbreaks of other classes. However, the positive cosine similarity could result from the representation degeneration issues, which find that the representations learned by Transformer models tend to clustered in a cone in representation space.

3. Subtracting jailbreak vectors may reduce ASR, but also potentially destroy the model parameters, making it hard for practice use. For example, in line 371, it may induce content repetition in the response. In addition, it also better if the performance of a general task can be included in this part for comparison.

### Questions
1.	In model settings, are the included LLMs trained with RLHF for safety issues? Will this affect the validity of analysis in this paper?

2.	The paper said no sampling is used when decoding. However, in practice, LLM based chatbots usually use sampling for diversity. This discrepancy may affect the conclusions in this paper. A study on the temperature selection can also verify the robustness of the proposed method.

3.	The paper uses middle layers for calculating jailbreak. Did you try the lower or upper layers? Or maybe an ablation study can further enhance our understanding. 

4.	In Section 4.4, the harmless dataset was generated by instructing ChatGPT. Were these samples checked by human annotators to guarantee the data quality?

5.	In line 256, the LLMs do not behave the same. What affects this, data or architecture?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper provides an empirical understanding about jailbreak success, specifically focused on the activation vectors. Authors hypothesized that jailbreak attacks with different attacks will have lead to similar underlying intermediate vectors from the language model, and this "jailbreak vector" can be used to promote or suppress the harmful behaviors. Their empirical results validate their claim, showing that (1) different jailbreak steering vectors have high cosine similarities (in Figure 3) and (2) these vectors can be transferred so that jailbreak vector from tactic A can be used to make model safer on tactic B (and other tactics). 

The paper further discussed about the hypothesis that jailbreaking attacks lead LMs fail to detect the harmfulness of the prompt, which is previously argued in Zou et al, 2023. The paper showed the result of PCA anaylsis (in Figure 5) and cosine similarity plots (in Figure 6) to show that jailbreaking often leads to the reducing the harmful features from the harmful instructions. But it also mentioned that low harmfulness always lead to low ASR score.

### Strengths
The paper is well-written and the claim is clear.

This paper presents clear empirical observations through multiple experiments about their claim that jailbreak vector exists. The authors tested on multiple LMs (7B-14B models) and tested multiple jailbreak tactics. Also, this claim is meaningful to understand the jailbreak success, and can be used to steer LMs to behave safer without additional fine-tuning.

The paper seems not to over-claim but tried to present their results objectively. For example, in Section 5.4, authors discussed about the harmfulness suppression, mentioning the exceptional cases where low harmfulness scores do not lead to low ASR scores. This helps readers and future researchers to understand the phenomenon in better ways.

### Weaknesses
I can't find significant weaknesses from the paper, though I think the paper could be improved if the authors include automatic jailbreak attacks like PAIR or TAP. These attacks don't specify the type of attacks but LLMs automatically find the attack. I think understanding their jailbreak success using latent space dynamics can be helpful to build successful defenses on such attacks.

### Questions
- There are bunch of automatic jailbreaking attacks that are trying not to use pre-defined tactics but discover different tactics using LLMs or other optimization-based approaches (for example, TAP or PAIR.) Do these attacks conclude to similar results?
- I wonder this observation can be also applicable to the safety-trained models -- for example, Llama2 or Llama3 are known to have low ASR on well-known jailbreak attacks due to safety training such as SFT or RLHF. Have you tried studying the vectors from these models?

### Soundness
3

### Presentation
4

### Contribution
3
