# RAIN: Your Language Models Can Align Themselves without Finetuning

- Decision: Accept
- Avg Score: 6.00
- Scores: 5, 8, 6, 6, 5

## Abstract
\vspace{-0.2cm}
Large language models (LLMs) often demonstrate inconsistencies with human preferences. Previous research typically gathered human preference data and then aligned the pre-trained models using reinforcement learning or instruction tuning, a.k.a. the finetuning step. In contrast, aligning frozen LLMs without requiring alignment data is more appealing. This work explores the potential of the latter setting. We discover that by integrating self-evaluation and rewind mechanisms, unaligned LLMs can directly produce responses consistent with human preferences via self-boosting. We introduce a novel inference method, Rewindable Auto-regressive INference (RAIN), that allows pre-trained LLMs to evaluate their own generation and use the evaluation results to guide rewind and generation for AI safety. Notably, RAIN operates without the need of extra data for model alignment and abstains from any training, gradient computation, or parameter updates. Experimental results evaluated by GPT-4 and humans demonstrate the effectiveness of RAIN: on the HH dataset, RAIN improves the harmlessness rate of LLaMA 30B from 82\% of vanilla inference to 97\%, while maintaining the helpfulness rate. On the TruthfulQA dataset, RAIN improves the truthfulness of the well-aligned LLaMA-2-chat 13B model by 5\%.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper is interested in *self-alignement*, i.e to align a model with human values without external supervision. Instead of proposing a method involving fine-tuning or any parameter update, it investigates a *rewind* mechanism during the inference phase, which, coupled with self-evaluation, allows the model to appraise generated text and only output something after having evaluated and eventually retraced its steps. The authors advertise three main advantages for their approach: being applicable to any model using auto-regressive inference, keeping the model frozen with no parameter update necessary, and not necessitating human supervision. 

The paper presents related work on alignment with and without reinforcement learning, and backtracking in inference, then, the method, Rewindable Auto-regressive Inference (RAIN), which consists in an *inner* and an *outer* loops. Assuming a tree structure representing the next possible token sets,
- The inner loop picks a leaf set, trying to balance exploration and exploitation of the token set value, and eventually extends the tree if necessary. It computes scores using a *self-evaluating prompt* which is used to update values for the parents in the tree (and the rest of the tree, through similarity of embeddings of token sets). It then samples new token sets. 
- The outer loop uses attributes (probabilities, values, and number of visits from the inner loops) to pick the next token set to be generated, similarly to a classical inference method. 

The authors evaluate their approach with 4 tasks: Harm-free generation, robustness to adversarial harmful generation, truthful generation, and controlled generation. The result of the model's generation process on these tasks is then evaluated by GPT-3 and 4 models, and human evaluation is further carried out on Harm-free generation. The authors also analyse their model, looking at sample and time efficiency, the accuracy of self-evaluation in the inner loop, and performing an ablation study.

### Strengths
- This paper proposes an approach for self-alignment, requiring no human supervision, no training, and largely applicable, based on a inner loop in the inference phase which exploits mechanism from reinforcement learning (usually employed in alignment) and employs a score given by the model itself. 
- The paper presents several experiments, among them testing their method on harmless generation, showing its efficiency through automatic and human evaluation.

### Weaknesses
 - The paper is a little difficult to follow, and I believe section 3.1 and parts of section 3.2 could be improved for a better presentation of the method.
- While the main experiment (being the main motivation of the paper) shows convincing results, I found several issues with the others:
    - While I can see its interest, I believe the robustness experiment should be better introduced and motivated in the paper.
    - Similarly, truthfulness can obviously be linked to harmlessness - still, I would have liked this to be discussed to better motivate the experiment.
    - Lastly, I do not completely understand the relevance of controlled generation.
    - While I understand that this may already common practice, having almost all of the production of your model evaluated by pre-existing model - which, furthermore, are not even public (nor is their training data) is something I believe to be an issue and should be **at least discussed** in the paper. 
- The method completely relies on a self-evaluation measure, in a form of a prompt. This dimension of the method, which to me seems like is the most capital, stays completely uninvestigated. Have other prompts be tested ? With a different keyword (harmful/harmless) ? How do naïve baselines (using a pre-trained binary classifier in place of self-evaluation, or using the current prompt without the inner loop but in the context of naive generate and evaluate) compare in term of running time and performance ?

### Questions
- I believe Figure 2 should be capital to the understanding of your method - however, the text helped me understanding the figure. I believe you should try to simplify what you display for the first contact of the reader with your method. 
- A large part of your citations are preprints - if those papers have been published, please update their reference. 
- While I appreciate your ablation studies, I believe those aspects of your method are all well-motivated. If you did not implement ablation studies for other mechanisms in your method, did you have any preliminary results showing the importance of them, or motivating your choices ?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper presents an intriguing and innovative method called Rewindable Auto-regressive INference (RAIN) to address the alignment problem of large language models (LLMs). Unlike previous fine-tuning-based approaches such as DPO, RLHF, and RAFT, which require additional data and optimization processes, the proposed method leverages LLMs' self-evaluation capacity and rewind decoding method to enable LLMs to align themselves with plausible preferences. It resembles human weighing patterns, involving evaluation, backtracking, and the selection of optimal generation paths. It is worth noting that while RAIN shares similar decision-making logic with Tree-of-Thought, the targeted problems and detailed self-evaluation mechanisms are distinct.

In summary, this paper makes the following contributions:

1. It introduces a novel self-alignment method for LLMs that does not rely on additional training resources, opening up an exciting research direction for addressing LLM alignment.

2. It demonstrates that LLMs are capable of performing self-alignment. Moreover, compared to existing approaches, it achieves remarkable alignment performance while requiring fewer resources.

3. It enhances the safety of mainstream open-sourced LLMs such as LLaMA-family, Vicuna, Alpaca, etc., without compromising the helpfulness of their outputs.

### Strengths
1. **Significance**: Aligning LLMs with correct values is an issue of utmost importance in the development of trustworthy and secure AI. Previous approaches require the use of additional models or SFT data to train LLMs on alignment preferences, which significantly increases the training cost. The proposed method enables LLMs to align themselves without external data, thereby reducing the development cost of LLMs even further.

2. **Originality**: This paper is the first to propose the use of LLMs for self-alignment, which not only represents a highly novel contribution but also establishes a new research paradigm for LLM alignment. I am looking forward to further work that focuses on reducing the inference cost of self-alignment.

3. **Quality**: The paper is written in a clear and easily understandable manner. The algorithm explanation is well-supported with illustrative examples, aiding in comprehension. Furthermore, the experimental setup covers mainstream open-sourced LLMs, and the comparison experiments include discussions on other alignment methods, showcasing the thoroughness of the work.

### Weaknesses
1. **Clarity**: There are some minor clarity issues in this paper:
   - Algorithm 1 is not referenced in the main text, although it is presented in the methodology section. It would be helpful to mention Algorithm 1 and provide a brief explanation or reference to it where relevant.
   - In the evaluation and searching process, there are several thresholds mentioned, such as $T_m$ and $V$. It would be beneficial to clarify whether these thresholds have common settings or if they are benchmark-specific. The paper lacks a detailed explanation of how these thresholds are determined, and whether they are sensitive to different task characteristics. For instance, are these thresholds fixed values, or are they dynamically adjusted based on the task or the LLM's performance during the self-alignment process? Furthermore, the paper does not discuss the potential impact of these thresholds on the overall performance and efficiency of the method. A more thorough analysis of their role is needed.


### Questions
1. In the inner loop, could alternative LLMs be utilized for conducting evaluation? What are your thoughts on the potential benefits of employing multi-agent debating for self-evaluation?

2. RAIN employs the embedding of pre-trained Sentence-BERT for calculating cosine similarity. How do you perceive the possibility of replacing it with the embedding from the LLM itself?

### Soundness
3 good

### Presentation
3 good

### Contribution
4 excellent

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a new inference-time method to align LLMs' output to human preference via nested iterations. In the outer loop, the algorithm will run the subsequence generation process ("inner loop"), concatenate subsequences to the final outputs, and keep checking whether the current generated sequence already contains the end-of-sequence token. In the inner loop, the proposed algorithm will generate sub-sequences via an iterative search process: 1) doing lookahead planning in a tree-search paradigm ("forward") and 2) self-evaluating the newly added nodes and updating values for nodes in the current search tree through the node ("backward"). When the termination condition is reached (e.g., the maximum number of iterations, or the value of the most-visited child node from the root is larger than a certain threshold), this iterative search process ends. The output of this search process is the token sequence associated with the tree path from the most-visited child node from the root. The experiment result demonstrates the effectiveness of the proposed method over harm-free generation, adversarial harm-free generation, truthful generation, and controlled sentiment generations via both automatic generation and human evaluation, though induces significant computational overhead.

### Strengths
1. This paper provides a model-agnostic inference-time algorithm that can save the training cost of doing alignment, and it also provides evidence that incorporating self-evaluation in search-based decoding can help improve the model alignment. 

2. The authors have done extensive experiments on various tasks and models to verify the effectiveness of the proposed method via both automatic evaluation and human evaluation, which makes this paper more solid.

### Weaknesses
1. **Limited Applications**: The proposed nested iterative search algorithm significantly increases the computational overhead at inference time (>3.7x on 70B models, and >4.3x on 30B models), making it intractable for practical purposes as the running time for these large models are already very large. In the meanwhile, the tree-search operation makes it extremely hard to perform parallelized optimization and can induce significant I/O throughputs as many operations in this proposed algorithm may not be able to easily run on GPU, so batch inference will be much harder to implement, further increasing the real latency on the user side. Considering this significant computational overhead, it is not clear whether this performance gain reported in this paper is worth it -- maybe practitioners should instead sample many more outputs via some diversity-enforced sampling method [1] (parallelizable and has been largely optimized via various open-source libraries such as VLLM [2]), and apply a well-tuned reward model to pick up the best outputs (note that this best-of-K/rejection sampling method is not even listed as baseline in this work). 

2. **Partially-Justified Motivation, and perhaps Marginal Contributions**: The author argues that "Beyond performance, the primary goal of this paper is to investigate the feasibility of enabling self-alignment in fixed LLMs without fine-tuning or RL" (in Introduction). However, it is not clear the necessity of applying the proposed iterative tree-search algorithm to verify this feasibility. As the authors recognize in the paper, there are already several tree-search-style inference-time algorithms in adjusting LLM outputs (the author mentioned [3] in the paper, and I think [4] is also related), and the self-evaluation does not seem like a new contribution in decoding content planning to improve both LLM reasoning and alignment (e.g., [1,5,6]) without learning. Though these works may not run on the specific task set as the author, they do have the potential to be strong competitors and some of them have already achieved the verification that a "learning-free algorithm can improve alignment via self-evaluation".

3. **Weak Baselines**: As explained in the above points, best-of-K/reject sampling, and existing tree-search algorithm (without iterations and back-tracking. Introducing self-evaluation to them does not seem too hard -- correct me if I am wrong.) have full potential to be the strong competitors to the proposed method (some of them may have already been deployed somehow by companies), given sufficient computational budgets (perhaps 3-4x more than normal inference time, to make a fair comparison to the proposed algorithm). None of them is made as a baseline in this paper and the author mainly compares with vanilla auto-regressive generation, which is relatively weak. Note, this is not to say the author needs to achieve state-of-the-art when comparing with these stronger baselines -- this is to help users understand the necessity of deploying the proposed algorithm and choose based on their needs. 

4. **Unclear Experiment Details**: What are the maximum number of iterations $T$ and the minimum number of iterations $T_m$ used in the experiment? How many tokens are generated for each node? Moreover, how does the author decide each hyperparameter for each task? I checked both the main text and appendix and I did not find how the author set these parameters and based on what observations. These parameters (especially $T$ and $T_m$)  can be very important for both reproduction purposes and for users to see a trade-off between efficiency and performance if they want to deploy the proposed method. 

5. **Hard-to-Read Formulation**: It is very hard to read the formulation presented in Section 3. For example, should not the `node` use different notations from the actual `token`? As each node contains more `attributes` (visit counts, embeddings) than a token? In many places, the authors use the same symbol to represent tokens and nodes. Also, $X$ and $Y$ sometimes seem interchangeable (e.g., $Y_{1:i-1}$ and $X_{1:i-1}$ as the "preceding context"). The usage of the subscript is not careful -- for example, why $S(Y)$ represents the score used to update $Y^*_{a:b}$ without having $a,b$ as input to $S()$?

### Questions
Most of my questions can be found in my "Weakness" section, I just list some here:
1. Why other inference-time algorithms are not listed as baselines? 
2. What are the detailed efficiency numbers (in detailed wall clock time instead of ratio) for your proposed method?
3. What are some missing hyperparameters? 
4. How do you decide them for each task? 
5. Can you review the formulation in Section 3 and update it to be more clear? 
6. Is there any possibility of achieving a better efficiency-performance trade-off using your method? For example, reducing the number of iterations?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes a new inference method called RAIN (Rewindable Auto-regressive INference) that allows large language models (LLMs) to align themselves with human preferences without requiring any finetuning or additional data.

- RAIN integrates self-evaluation and rewind mechanisms into the inference process. This allows the LLM to evaluate its own generated text, then "rewind" and modify the generation if needed to produce safer responses.
- Experiments on tasks like harm-free generation and truthful QA show RAIN improves alignment of fixed LLMs like LLaMA without finetuning. 
- Advantages include no need for alignment data, compatibility with frozen LLM. 

Overall, the paper demonstrates the feasibility of aligning fixed LLMs without any external data or training. RAIN provides an inference-time solution to improve safety and alignment that is user-friendly, resource-efficient, and broadly applicable.

### Strengths
The paper studies the important topic of aligning LLMs. The paper takes a specific angle of designing inference-time techniques to reduce the changes that models output harmful text.

### Weaknesses
 - The proposed inference-time method has high computational cost. This will make it challenging for the method to be deployed in practice. The method requires multiple forward passes through the model for each generation, which significantly increases the inference time compared to standard decoding algorithms like beam search or greedy decoding. The computational overhead is especially concerning for large language models with billions of parameters.
- The proposed method is complicated. The combination of Monte Carlo tree search, token similarity checks, and dynamic weight adjustments makes the algorithm difficult to understand and implement. The multiple steps involved in the rewind and forward generation process add to the complexity, making it challenging to debug and optimize.
- The authors use an umbrella "harmless" notation (for which the self-evaluation score is based on), whereas in practice whether something counts as harm can be contextual. The self-evaluation score relies on a single, generalized notion of harmlessness, which may not capture the nuances of different types of harm. For example, a response that is factually incorrect might be considered harmless in one context, but harmful in another, and the current approach does not account for such contextual variations.

### Questions
NA

I read the author response, and I am keeping my original score.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
**Summary**

The paper introduces an inference method called RAIN, which allows pre-trained language models to align themselves without the need for finetuning or extra alignment data. This method integrates self-evaluation and rewind mechanisms to produce responses consistent with human preferences via self-boosting. The authors demonstrate the effectiveness of RAIN in improving the harmlessness and truthfulness rates of pre-trained language models through experiments on several benchmark datasets.

### Strengths
**Pros**

1. No need for extra alignment data: RAIN does not require any additional data for model alignment, which can save time and resources. This is because RAIN uses self-evaluation and rewind mechanisms to align the model, which allows it to learn from its own mistakes and improve its performance without the need for external supervision.

2. Improves model safety: RAIN can improve the harmlessness and truthfulness rates of pre-trained language models, which can make them safer to use in real-world applications. This is because RAIN allows the model to produce responses that are consistent with human preferences, which can reduce the risk of the model generating harmful or misleading outputs.

### Weaknesses
 **Cons**

1. Limited to fixed pre-trained models: RAIN is designed to align fixed pre-trained language models and cannot be used to align models that are being trained or fine-tuned. This means that RAIN may not be suitable for applications that require continuous model alignment or adaptation.

2. Baselines: The paper does not provide a detailed comparison of RAIN with other methods that align pre-trained language models using RLHF or instruction tuning.

3. Limited evaluation on real-world scenarios: The experiments in the paper are conducted on benchmark datasets and may not fully capture the complexity and diversity of real-world scenarios. This means that the effectiveness of RAIN in real-world applications may be different from what is reported in the paper.

4. Computation burden: The method has a high computational cost. This will make it challenging for the method to be deployed in practice.

### Questions
**Questions for the authors**

How does RAIN compare to other methods that align pre-trained language models using reinforcement learning or instruction tuning?

What are the potential limitations or drawbacks of RAIN, and how can they be addressed in future work?

How scalable is RAIN to larger models or datasets, and what are the computational requirements for using RAIN on such datasets?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair
