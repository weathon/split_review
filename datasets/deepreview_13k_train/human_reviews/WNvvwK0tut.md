# Scaling up Masked Diffusion Models on Text

- Decision: Accept
- Scores: 6, 8, 6, 6

## Abstract
Masked diffusion models (MDMs) have shown promise in language modeling, yet their scalability and effectiveness in core language tasks, such as text generation and language understanding, remain underexplored. This paper establishes the first scaling law for MDMs, demonstrating a scaling rate comparable to autoregressive models (ARMs) and a relatively small compute gap. Motivated by their scalability, we train a family of MDMs with up to 1.1 billion (B) parameters to systematically evaluate their performance against ARMs of comparable or larger sizes. Fully leveraging the probabilistic formulation of MDMs, we propose a simple yet effective \emph{unsupervised classifier-free guidance} that effectively exploits large-scale unpaired data, boosting performance for conditional inference. In language understanding, a 1.1B MDM shows competitive results, outperforming the larger 1.5B GPT-2 model on four out of eight zero-shot benchmarks. In text generation, MDMs provide a flexible trade-off compared to ARMs utilizing KV-cache: MDMs match the performance of ARMs while being 1.4 times faster, or achieve higher quality than ARMs at a higher computational cost. Moreover, MDMs address challenging tasks for ARMs by effectively handling bidirectional reasoning and adapting to temporal shifts in data. Notably, a 1.1B MDM breaks the \emph{reverse curse} encountered by much larger ARMs with significantly more data and computation, such as Llama-2 (13B) and GPT-3 (175B).

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
Note: The authors addressed my concerns about disentangling masking and diffusion in their response with an additional experiment. I thus adjusted my score from 5 to 6.

-------

The paper studies scaling up masked diffusion models (MDMs) for text. The first establish scaling laws for MDMs and compare them to autoregressive models. They also propose an unsupervised CFG (classifier-free guidance) technique (based on Ho & Salimans, 2022, Chang et al. 2023) to boost performance with only unlabeled data. 

The results show that:
-ARMs and MDMs demonstrate competitive scaling rates and similar scaling behavior (the compute cost of achieving a particular validation loss z with an MDM is 16x higher than that of achieving that loss z with ARMs but this factor stays constant)

-Unsupervised CFG gives consistent gains over vanilla MDM across all the 8 QA tasks.

-MDM and ARM, when given same compute achieve similar performance (but MDM achieves strong performance when trained for 16x longer).  1.B MDM performs comparably to a 1.5B GPT-2.

-MDM has success breaking the reverse curse.

### Strengths
-Exploring diffusion models for text is an interesting direction. The authors' work is well motivated. 

-The gains from Unsupervised CFG seem consistent across the 8 tasks.

### Weaknesses
-I believe comparing to a a text-based LLM that uses bidrectional masking/span corruption is more fair than a left-to-right next token prediction ARM model like GPT2. This would disentangle the value of the masking (which can also be done in language models) from the diffiusion aspect.

Right now I think these two factors are conflated. For example are the reverse curve results in Table 6 because the MDM uses masking or because its a diffusion model?

-The novelty of the work is also modest.

### Questions
-Please see the Weaknesses above.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper scaled up Mask Diffusion Model based on previous work [1], demonstrate that previous work has strong scalability of Masked Diffusion Model for text. The paper also fit the scaling law of MDM, and found that MDM need 16x more training computation to match the validation loss of AutoRegressive model. 

The paper also employed simple yet effective classifier free guidance (CFG) for MDM that improved the performance of downstream tasks. 

Finally the authors evaluated the model on reverse curse, a challenging problem of autoregressive language model, and showed that MDM alleviate the reverse curse greatly. 



[1] Your Absorbing Discrete Diffusion Secretly Models the Conditional Distributions of Clean Data

### Strengths
1. The paper scaled up the Masked Diffusion Model(MDM) for text, and experiment are performed in a solid to demonstrate the strength (bidirectional modeling of text), and weakness (has to consume more computation to reach the performance of AR language model).


2. The paper provided the research community with understanding of MDM in term of scaling and future research directions of more computationally efficient MDM, which is a significant contribution. 


3. The paper is written in a clear and easy to follow way. 


4. The supplementary materials are sufficient to review or reproduce this work.

### Weaknesses
1. The major theoretical basis are given in the previous work [1], this work only performed experiments to scale up, which makes this paper less impressive and novel. 

2. In the reverse curse experiment (Table 6), it seems that MDM performance still decay in reverse direction in two dataset. Given the model encodes the text in a bidirectional way, how we can explain this decay ?

3. There are minor typo problems.

### Questions
1. See `2` of Weakness 

2. For CFG based generation, it seems that we need double computation to compute $\tilde{p}$. So are the results in Table 1 using the same sampling steps ? If so, is it possible that the extra computation contribution to performance improvement ? It could be better to use a doubled sampling step w/o CFG to compare the performance so that we can rule out the hypnosis

3. In Line 756  and Line 777, `Greddy` or `Greedy` ?

### Soundness
3

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
3

### Summary
The paper focuses on scaling Masked Diffusion Models (MDMs) as an alternative to Autoregressive Models (ARMs) in language modeling.  The study establishes the first scaling law for MDMs, indicating that they can achieve performance on par with ARMs at a smaller computational cost gap than previously assumed. Moreover, MDMs demonstrate competitive performance in zero-shot language understanding tasks and effectively address ARM challenges like "reversal curse" and temporal quality degradation.

### Strengths
-   The introduction of scaling law for MDMs trained from scratch suggests that they show the same scaling potential as ARMs.
-   The presentation is clear and well-organized, with only minor typos.
-   Results on reversal curse tasks of MDMs is strikingly better than ARMs. This is an interesting point.

### Weaknesses
 	extbf{Unfair Comparison:} Line 368-369: The authors extend MDM pre-training time by a factor of 16 to achieve a “meaningful” comparison with ARMs. However, a more valid comparison would involve MDMs and ARMs trained with equivalent compute budgets or trained to convergence for a given model size. Comparing an MDM to an ARM trained with only 1/16 of its FLOPs does not yield a balanced assessment. This makes it difficult to draw conclusions about the relative efficiency of MDMs versus ARMs, especially in conditional generation tasks. The reported results are therefore misleading, as they do not reflect a fair comparison of the models' capabilities under similar training constraints.

	extbf{Missing Citations:} The paper lacks a related work section, making it difficult for readers unfamiliar with text DMs. Notably, a closely related work [1] is omitted. This prior research examines scaling trends of MDMs fine-tuned from a pretrained MLM and evaluates MDMs on complex tasks, aligning closely with this paper's contributions. The absence of this citation is a significant oversight, as it fails to acknowledge relevant prior work that directly addresses similar research questions and methodologies.

	extbf{Weak Benchmarks:} The benchmarks used in section 5 are mostly language understanding tasks, i.e, can be mostly formulated as a one-token-completion task. These NLU tasks are of less interest now, compared to summary benchmarks like gigaword and reasoning benchmarks like GSM8K, which require more complex abilities. The current benchmarks do not adequately assess the models' ability to handle more complex generation tasks or multi-step reasoning, which are crucial for evaluating the true potential of language models.

	extbf{Typos:} 

Line 458 RELEVING should be relieving

Line 756 & 777 greddy should be greddy

### Questions
It is acceptable that MDMs trained from scratch do not match the performance of ARMs, as suggested by the scaling law in this paper as well as previous text DM work. I think a better way to present these findings should be reporting both the pros and cons of MDMs, e.g., they are more computation-consuming but can perform some tasks that state-of-the-art ARMs cannot do at all.

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper explores the potential of Masked Diffusion Models (MDMs) in language tasks, highlighting their scalability and performance compared to autoregressive models (ARMs). The authors train models with up to 1.1 billion parameters and demonstrate a scaling law for MDMs. MDMs show competitive results in language understanding and provide a flexible trade-off in conditional generation compared to ARMs. Additionally, the authors find MDMs are robust to temporal shifts in data and overcome the reverse curse problem faced by ARMs.

### Strengths
- Scaling MDM: The main contribution of this paper lies in scaling mask discrete diffusion (MDM) and provide the corresponding scaling law.
- Identifying distinctive features of diffusion: The authors highlight how diffusion can effectively address shortcomings like temporal shifts in data and the reverse curse found in ARM. This paves the way for additional research and application opportunities in the realm of diffusion language models.

### Weaknesses
 - The paper primarily compares MDM and AR, but lacks a clear comparison with other pretrained diffusion language models such as Plaid (https://arxiv.org/abs/2305.18619) and SEDD (https://arxiv.org/abs/2310.16834) under the same setting. 
- The diffusion loss provides an upper bound and should not be directly compared with the loss in AR models. The comparison in Figure 2(a) appear to lack rigor, a similar problem for the perplexity comparison detailed in Table 7.
- About the setup described in Table 6, it appears that MDM fine-tuned on the dataset, while GPT3 and LLaMA not. To mitigate the potential confounding variable of fine-tuning versus prompting, a baseline model like fine-tuned GPT-2 ought to be included for a more comprehensive analysis.
- The proposed unsupervised CFG is similar to calibration in AR (http://arxiv.org/abs/2102.09690,http://arxiv.org/abs/2104.08315), but the relationship is not properly discussed.

Minor:
- typo: line 756 “Greddy sampling“

### Questions
- Why different likelihood evaluation methods result in distinct behavior on different tasks? How can we decide on the fly given a new task?
- What's the relationship between 10^20 Flops and tokens? Do both ARM and MDM consume the same amount of tokens?
- What’s the inference timesteps in Table 5? Line 409 “Built upon the unsupervised CFG”, does it means the inference timesteps are doubled? It's better to draw a curve to show the speed advantage of diffusion, which I guess is in generating longer texts.
- What’s the computation resource and GPU hours comparison for MDM and AR?

### Soundness
3

### Presentation
3

### Contribution
3
