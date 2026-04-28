# Chat Vector: A Simple Approach to Equip LLMs With New Language Chat Capabilities

- Decision: Reject
- Avg Score: 5.25
- Scores: 5, 6, 5, 5

## Abstract
With the advancements in conversational AI, such as ChatGPT, this paper focuses on exploring developing Large Language Models (LLMs) for non-English languages, especially emphasizing alignment with human preferences. We introduce a computationally efficient method, leveraging “chat vector,” to synergize pre-existing knowledge and behaviors in LLMs, restructuring the conventional training paradigm from continual pretrain $\rightarrow$ SFT $\rightarrow$ RLHF to continual pretrain + chat. Our empirical studies, primarily focused on Traditional Chinese, employ LLaMA2 as the base model and acquire the chat vector by subtracting the pre-trained weights, LLaMA2, from the weights of LLaMA2-chat. Evaluating from three distinct facets, which are toxicity, ability of instruction following and multi-turn dialogue demonstrates the chat vector's superior efficacy in “chatting”. To confirm the adaptability of our approach, we extend our experiments to include models pre-trained in both Korean and Simplified Chinese, illustrating the versatility of our methodology. Overall, we present a significant solution in aligning LLMs with human preferences efficiently across various languages, accomplished by the chat vector.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This manuscript presents an innovative concept that focuses on transferring the chat functionalities of large language models (LLMs) to an additional linguistic domain. The rationale is based on leveraging the "task vector" inherent within pre-trained models, viewing conversation as a distinct task. The empirical study utilizes the LLaMA2 framework, aiming to extract and apply the conversational task vector from LLMs trained on Simplified Chinese and Korean to a Traditional Chinese setting.

### Strengths
1. The subject matter of extending the utility of LLMs to encompass a broader range of languages is of significant relevance, and the authors approach this with a methodology that is both novel and straightforward.

2. The manuscript is well-structured, particularly in the introduction, review of related literature, and methodological explanation, allowing for clear comprehension of the proposed ideas.

3. The paper addresses a pertinent area of LLM research, offering insights that I recommend for review by fellow researchers in the field.

### Weaknesses
1. The methodological framework introduced appears to be in its nascent stages and could benefit from a more robust theoretical underpinning. The authors' approach of utilizing the entirety of the chat vector from the model warrants further exploration. A more granular analysis, such as the selective use of model parameters (for instance, only the feedforward neural network layers), may enhance the efficacy of the transfer and minimize unintended model behaviors. This suggestion is not to imply that the simplicity of the method is a drawback; rather, a more in-depth investigation could yield richer contributions to the field.

2. The experimental design, while based on an appealing premise, is somewhat limited in scope. The paper's evaluation focuses solely on Traditional Chinese as the new language, with Simplified Chinese as the source. Given the linguistic similarities between these two variants of Chinese, the challenge for the LLMs may be less pronounced, which in turn affects the persuasiveness of the results. It is recommended that subsequent iterations of the research consider a more diverse set of language pairs to strengthen the validity of the experimental findings.

3. There is room for improvement in the clarity and presentation of the data, especially in the main results table (referred to as Table 1 in the manuscript). For instance, if all experimental configurations require continual pretraining (CP), it may be redundant to list this in the table. A more streamlined presentation could assist readers in readily identifying the critical findings of the study.

### Questions
Refer to the above.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
What is this paper about, what contributions does it make?
This paper focuses on developing Large Language Models (LLMs) for non-English languages, emphasizing alignment with human preferences. The method  leverages chat vector to synergize pre-existing knowledge and behaviors in LLMs. It  enables Large Language Models (LLMs) to exhibit conversational skills by incorporating the chat vector into the model. The method is evaluated on toxicity, ability of instruction following, and multi-turn dialogue. 

What contributions does it make: 
The paper introduces an approach to enable Large Language Models(LLMs) to exhibit conversational skills and operate in accordance with human expectations in a target language by incorporating the chat vector into the model with the same architecture.

### Strengths
1.The method can can be used for multiple languages. 
2.The chat vector proposed by the paper simplifies the traditional training paradigm.

### Weaknesses
1.It is not intuitive that a chat vector can represents the parameter difference between a chat model and PLM. More interpretable experiments are needed here. 
2.The novelty of this paper is limited as the idea stems from Ilharco et al. (2023).
3.The paper does not mention the details of parameters setting, which is not easy for others to reproduce and use.
4.The experiment is built on LLaMA as well as the baselines. Other base LLMs are encouraged to be included.
5.The text in the picture is too small.

### Questions
What is distinct contribution of this paper comparing with Ilharco et al. (2023)?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes to adopt a the difference vector between LLAMA2 and LLAMA2-Chat as a Chat Vector and achieves computational efficient linguistic transfer on other languages, e.g. Traditional Chinese. The method is incredibly easy and might bring some potential to achieve efficient linguistic transfer for Large Language Models. The authors conduct experiments on three languages across various task completion benchmarks to demonstrate the effectiveness of the method.

### Strengths
1. The proposed method is incredibly easy. If it is solid, the linguistic transfer from high-quality LLAMA to other LLMs will be incredibly efficient and easy.

2. The paper focuses on developing LLMs for people using minor-languages, which is huge contributions.

### Weaknesses
1. The theoretical basis for Chat Vector is too weak. The task vector which motivates this paper is reasonable in its hypothesis. The task vector can be regarded as a kind of meta-learning setting, in which the pre-trained LLM is close to a near-convergence and general point in the meta-learning space and the task-specific fine-tuning can drive the model to the task-specific convergence. In this way, such task vector can be regarded as a vector pointing from the general LLM point to the task-specific point. However, if we transfer the task vector to your chat vector, your task is a multi-task learning manner to align LLM with human preference. In this way, what is the meaning or physical representation of such chat vector? The authors need to provide a more rigorous justification for why the difference between the weights of a base model and its instruction-tuned variant would yield a transferable representation of instruction-following ability. It's not clear that this difference vector captures a coherent concept, especially given that instruction tuning involves complex changes across the entire network, not just a simple shift in a single direction. The analogy to task vectors is not strong enough to justify the approach without further theoretical backing.

2. The evaluation is not sufficient to demonstrate the effectiveness. Please also consider to add MT-Bench, MMLU, which are more commonly used to evaluate the performance of LLMs. The current evaluation focuses on a limited set of tasks and does not provide a comprehensive picture of the model's capabilities. The absence of standard benchmarks like MT-Bench, which assesses conversational ability, and MMLU, which evaluates knowledge and reasoning, makes it difficult to compare the proposed method with existing approaches. The paper needs to demonstrate that the method improves not just on the specific tasks tested, but also on a broader range of capabilities that are typically evaluated in LLMs.

3. I have some concerns with the fairness of the experiments. Considering that the CP process only involves 3.1B tokens, the model after CP is less likely to be trained well to the Traditional Chinese domain. (The pre-training of LLAMA involves 2.4T tokens, 3.1B is only 0.13%). In this way, your baseline CP+FT is underfitting and has not converged, making it as a weak baseline. It is easy to demonstrate this hypothesis that the gap between CP+FT and CP+FT+Chat Vector on Chinese-LLAMA is much less than that on Traditional Chinese LLAMA you trained. This is because that the pre-training for Chinese-LLAMA is 120GB corpus, which is much sufficient to adapt LLAMA to the new language. Chinese-LLAMA is also not trained well but the performance improvement is not remarkable compared with the improvement on Traditional Chinese. I guess there might be some scaling law here. If your CP is sufficient and scaled up, you might finally found that the Chat Vector's contribution is less. The concern about the baseline's underfitting is significant. The authors should provide evidence that the baseline model is sufficiently trained before comparing it to the proposed method. The current experimental setup makes it difficult to isolate the effect of the chat vector from the effect of simply having a better-trained model. The authors should also investigate the impact of scaling up the CP process and see if the effectiveness of the chat vector diminishes with more pre-training data.

### Questions
1. Why you did not translate your fine-tuning dataset to Korean and Simplified Chinese? In this way, you can start with Chinese-LLAMA and Korean-LLAMA to do the same fine-tuning process, which makes the comparisons across different languages much more fair.

2. What is the evaluation benchmark reported in Table 1? Is it Vicuna Benchmark?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work proposes an approach to swiftly equip the chat capability to a LLM of a new language, by leveraging the "chat vector" based on the concept of "task vector" proposed by Ilharco et al., 2023. Specifically, "chat vector" is simply the weight difference between a plain LLM and its chat-finetuned version (on English LLaMA), which represents the acquired chat ability of the LLM, and can be synergized through vector addition on a new LLM. The authors conduct experiments primarily on Traditional Chinese, examining the instruction following, multi-turn dialogue and toxicity after applying "chat vector" on Traditional Chinese LLaMA.

### Strengths
- This works presents an interesting perspective to adapt chat capability to LLMs by directly applying the idea of "task vector", which is extremely simple and does not require any training. This can be a direction to further investigate in future research, complementary to the SFT/RLHF training.
- A new dataset for SFT in Traditional Chinese is also introduced through "self-instruct", which can be a good resource for community if it is released.

### Weaknesses
I found the evaluation has certain flaws as follows:

- The evaluation on the instruction following adopts GPT4 to provide a score on how close the LLM's response is to the GPT4's response. This process could have large variance, and a low score does not necessarily mean a bad response (since only one reference from GPT4 is being compared). To the extreme extend, if we ask GPT4 to generate a new response, and compare with its old response, the score might also be low. Without showing the variance, I don't think this protocol could evaluate the response reliably. It is mentioned in Section 4.3 that this decision is to avoid calling GPT4 n^2 times (n being the number of models to compare); however, I would suggest to at least compare these two models in this way: "llama2 → CP → FT" and "llama2 → CP + chat vector", to better evaluate the performance of adding "chat vector".
  
- Obtaining the chat capability by simply adding "chat vector" on a new LLM seems too good to be true, and it would be good to provide some qualitative responses, providing more insights on its effect. However, the paper did not show any responses by adding "chat vector" alone. The only example shown in Figure 2 is when combining SFT with chat vector together. It is not directly convincing that by adding chat vector, "llama2 → CP + chat vector" is able to perform better than "llama2 → CP → FT" according to human standards; more evidence needs to be shown in addition to Table 1.

### Questions
See weaknesses.

Also, for the same example shown in Figure 2, is it possible to also provide the response from the version "llama2 → CP + chat vector"?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
