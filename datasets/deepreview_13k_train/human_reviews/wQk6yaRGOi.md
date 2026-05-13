# Improving Discrete Diffusion with Schedule-Conditioning

- Decision: Reject
- Scores: 8, 6, 6, 6

## Abstract
Discrete diffusion models, like continuous diffusion models, generate high-quality sequence data by gradually undoing noise applied to datapoints via a Markov process. Gradual generation in theory comes with many conceptual benefits; for example, inductive biases can be incorporated into the noising Markov process. In practice however, the best performing discrete diffusion model is consistently masking, which does not denoise gradually. Here we explain the performance of masking diffusion by noting that it makes use of a fundamental difference between continuous and discrete Markov processes: discrete Markov processes evolve by discontinuous jumps at a fixed rate and, unlike other discrete diffusion models, masking diffusion builds in the known distribution of jump times and only learns where to jump to. We show that we can similarly bake in the known distribution of jump times into any discrete diffusion model; despite their simplicity, our new models -- schedule-conditioned diffusion (SCUD) -- generalize classical discrete diffusion and masking diffusion. By applying SCUD to models with noising processes that incorporate inductive biases on images, text, and protein data, we build diffusion models that outperform masking.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The choice of forward process has great performance implications for (discrete) diffusion models. This paper theoretically studies the improved performance of the masking forward process in discrete diffusion models. To this end, the authors introduce the notion of an event schedule, which describe times along the forward process where transitions take place, and separate the "when" of transition from the "where" of transition. 

The authors further derive the training objectives corresponding to conditioning on these event schedules, and apply their proposed method SCUD, to the tasks of image generation, language generation and protein sequence generation. Across the different tasks, their proposed method is able to outperform equivalent forward processes, but without the conditioning using less training examples.

### Strengths
1. The main strength of the paper is the firm theoretical footing to understand different forward processes in discrete diffusion, and how they relate to the "when" and "where" of the corresponding transitions. Through the notion of event / schedule conditioning, the paper attempts to disentangle the influence of "when" and "where", which leads to corresponding modifications to the ELBO objective. The authors also emphasize the connections of their method to previous discrete diffusion methods. 

2. The paper is very well written, and makes a strong effort to coherently explain the different moving parts. 

3. To connect the method to practice, the authors also propose different tricks such as reversing multiple events jointly, and an efficient loss formulation for high-dimensional data. Experiments across image, protein and language domain show favorable improvements for the same forward process, conditioned on event schedule. The experiments on proteins are especially interesting, using 2 orders less of training data.

### Weaknesses
There are no glaring weaknesses in the paper. But there is some minor feedback:

1. The formal notion of event schedule is only introduced in Proposition 4.2. This should instead be moved to before Proposition 3.1, so the readers already know what the event schedule captures, and the corresponding equations become easier to follow.

2. There are claims in the paper regarding SCUD outperforming masking, but evidence of this is not visible in the experiments. It is unclear whether the SCUD conditioning with Gaussian / Uniform will outperforming existing discrete diffusion (e.g. D3PM) with masking, given equal compute. The experiments presented compare SCUD with structured forward processes to SCUD with a uniform forward process, which is argued to be similar to masking. However, a direct comparison with a standard masking diffusion model, such as D3PM, is missing. This makes it difficult to assess the true advantage of SCUD over established methods.

### Questions
1. In light of the point 2 in weaknesses, could the authors run the D3PM model with masking diffusion with the same number of training samples as SCUD? -- The reviewer hopes this is feasible within the available compute budget of the authors. An alternative would be to also consider small versions of D3PM and SCUD that can be trained for equivalent number of samples.

2. How is B defined in the language and protein experiments?

### Soundness
3

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
The paper presents Schedule Conditioned Diffusion (SCUD), a new method to enhance discrete diffusion models for conditional sequence generation. The authors identify that existing structured and state-dependent approaches are often outperformed by the simpler "masking diffusion," due to its effective alignment of forward and backward transition schedules. They introduce a decomposition of the Evidence Lower Bound (ELBO) that addresses this mismatch and demonstrate efficient training strategies for SCUD. The findings indicate that SCUD achieves similar performance to masking diffusion, with the authors releasing their code for further exploration.

### Strengths
- The paper is well written, equations are nicely embedded and overall presentation is good (marking will be raised to good once the page limit is achieved).

- The paper effectively addresses limitations of existing discrete diffusion models, specifically the dominance of masking diffusion over more gradual and structured processes. It provides a solid theoretical foundation to argue for the introduction of SCUD.

- Introducing the SCUD model, which conditions on the transition schedule, is a novel approach. This model adapts diffusion frameworks by incorporating structured forward processes, potentially expanding discrete diffusion's applications across data types.

- The paper includes a rigorous theoretical framework, with proofs and mathematical propositions that justify the SCUD approach.

- The experiments span various data types, including images, text, and protein sequences. Results on CIFAR-10, LM1B, and UniRef50 datasets convincingly show that SCUD improves performance compared to other non-masking processes.

- The paper compares SCUD with state-of-the-art discrete diffusion models, showing how SCUD better captures transition schedules and can leverage structured processes.

### Weaknesses
# Presentation (Minor)

I will re-adjust my mark for presentation from poor to good once the following urgent concern has been addressed by the authors:

- The text of the main paper exceeds the 10-page limit. Please move your remarks regarding Reproducibility to the appendix, ICLR will likely be strict about enforcing the 10-page limit, exceeding the limit may lead to your work being rejected down the line.


# Content (Major)

- The paper's complexity could limit practical adoption. SCUD requires intricate parameterizations and careful handling of components like the rate parameter $\gamma$ and the transition matrix $K$ in particular, potentially increasing computational cost.

-  While SCUD reduces training samples, the discussion on costs associated with complex matrix operations, schedule conditioning, and increased dimensionality in high-dimensional data is minimal.

- The qualitative analysis of CIFAR-10 images suggests that SCUD models lack clear object formation. Though the focus is on likelihood scores, this limitation in sample quality could affect its utility in image generation tasks.

### Questions
In general, I am willing to raise my score, if my concerns and questions are addressed with compelling evidence. 

Building on the aforementioned weaknesses, I pose the following questions:

1. Can you provide O-Notation w.r.t. the data-dimensionality for the added computational cost arising from $K$? Furthermore mentioning the GPU hours of the different methods in your work could help put the computational cost of different methods into perspective.

2. In addition to 1.: Could you provide a quantitative comparison of the computational costs associated with SCUD versus standard discrete diffusion methods in terms of memory usage and processing time?

3. Given the increased complexity SCUD introduces, what specific strategies could one use to manage computational demands when applying SCUD to larger datasets or higher-dimensional inputs?

4. Could you elaborate on how sensitive SCUD is to the selection of the rate parameter $\gamma $? How does this parameter interact with other hyperparameters in practice on datasets other than CIFAR-10 as shown in figure 2?

5. Are there particular domains where SCUD could have inherent advantages over masking diffusion?

6. Although SCUD improves likelihood scores, how do you plan to address the relatively low quality of visual samples generated in CIFAR-10? Could modifications to SCUD enhance sample fidelity?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
1

### Summary
This paper propose that masking diffusion succeeds because it leverages information about when corruption events occurred, enabling it to focus on modeling relationships between tokens rather than inferring corruption events. Building on this insight, they introduce a new method called schedule-conditioned diffusion (SCUD), which incorporates corruption schedule information into discrete diffusion models. Experimental results demonstrate that SCUD generalizes masking diffusion and outperforms classical discrete diffusion methods on various datasets.

### Strengths
​1. **Innovative Insight**: This paper provides a novel explanation for the success of masking diffusion, linking it to the modeling of corruption schedules, which is a valuable addition to the understanding of discrete diffusion processes.

​2. **Methodology**: The introduction of SCUD is rigorous, with mathematically supported schedule conditioning, which extends masking diffusion and further enhances its performance.

​3. **Empirical Evidence**: Experiments on image, text, and protein data show that SCUD outperforms standard discrete diffusion models, supporting its claims of enhanced generative capability.

### Weaknesses
​1. **Lack of Motivation Explanation**: The authors seem to focus heavily on explaining how SCUD works, with less emphasis on why this approach is chosen and what its ultimate goal is. This may make it difficult for readers to follow the authors’ line of reasoning. Specifically, the paper lacks a clear articulation of the limitations of existing discrete diffusion models that SCUD aims to address. There's no discussion of why learning the transition schedule is crucial for improving performance, and how this relates to the underlying data generation process. Without this context, the reader is left wondering about the practical significance of the proposed method.

​2. **Over-Reliance on Appendix for Proofs**: Many key proofs and details are placed in the appendix, which disrupts the main text’s coherence and could interfere with readers’ logical understanding. For example, the proofs for the core theoretical results are not presented in the main body, making it hard to follow the logical flow and assess the validity of the claims. This makes the paper feel incomplete and forces the reader to constantly switch between the main text and the appendix, which hinders comprehension.

​3. **Inadequate Training/Sampling Procedure Description**: The description of the training and sampling processes is not sufficiently detailed, making it difficult to understand SCUD’s training and sampling mechanics without referring to supplementary materials or  external resources. The paper does not provide a step-by-step algorithmic description of how SCUD is trained and used for generation. Key details such as the specific loss function used, the optimization algorithm, and the sampling strategy are missing, making it difficult for other researchers to replicate the results or build upon this work.

### Questions
​1.	Could the authors clarify the role of $\Delta t$ in discrete Markov process? This is not clearly defined in the “Background” section, nor are there references provided for further reading.

​2.	Would it be possible to simplify some of the proofs to make them more accessible in the main text?

​3.	Why didn't provide the complete training and inference process in algorithmic form in the paper?

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
4

### Summary
This paper attempts to understand the empirical finding that discrete diffusion models using a masking corruption process outperform other noising processes such as uniform or Gaussian noising processes in which tokens are "mutated." The authors hypothesize that masking diffusion dominates due to having knowledge of when corruptions occur, which is not the case for the non-masking noise processes. With this hypothesis, the authors propose a modification to standard non-masking discrete diffusion models that allows the model to condition on information about the schedule of the noising process. The authors derive a new version of the ELBO used to train discrete diffusion models into one that explicitly marginalizes over different noise schedules. This allows them to propose a new training objective and parameterization of the denoising process that conditions on noise schedules. The authors evaluate their approach on images, text, and proteins and demonstrate that their approach consistently improves over models using the same noising process, but without schedule conditioning.

### Strengths
The paper is tackling an original problem, namely understanding why masking discrete diffusion outperforms other noising processes including those that have domain-specific inductive biases. While I have some concerns with the hypothesis (see section Weaknesses), I agree that conditioning on noise schedules should help mitigate some of the advantages that masking diffusion models have. The paper contains a rigorous derivation that shows how to incorporate the noise schedules into the modeling framework. The empirical results demonstrate that conditioning on the noise schedule tends to improve likelihood-based metrics over models that use the same noise process but do not incorporate the noise schedule.

### Weaknesses
I am not convinced by the primary hypothesis outlined in the abstract that says "...we propose that masking diffusion dominates due to knowledge of when corruptions occur." Unless I am misunderstanding something, masking diffusion models have no knowledge of when an event occurs, only that an event occurred. To put a different way, the identity of the state (masked or not) tells us whether it has been noised. However, we have no idea when the noising occurred. This seems like an important point for motivating the use of noise schedules as input.
  
The primary weakness for me was the experimental results. In particular, the paper seems to be lacking several key details about the experiments. I will reiterate this in the "Questions" section, but I did not see any explanation for why the authors chose to model Cifar10 with both 128 and 256 pixel values. Based on the lack of explanation, I am left feeling that the B=128 experiments were done simply because this was a setting where the authors found they can get Gaussian SCUD to improve over Masking. However, to me, this makes the results appear cherry-picked. Furthermore, in Figure 2, it appears Gaussian is already outperforming Masking, without SCUD (although perhaps not with statistical significance), diminishing the novelty of the result. There should be some commentary on this since.

All of the experiments appear to be done with different training data than the baselines. Thus, I am not sure any of the numbers are truly valid in terms of comparing between methods. Most concerningly, I didn't see any explanation of this in the text or appendix. Baselines should be redone using the same training data.

For the baselines, it seems a crucial baseline would be to use all of the same hyperparameters as SCUD, but without conditioning. This would use the same noising process (e.g. Gaussian or Uniform), the same architecture, and the same training data but without using any conditioning information (e.g. just pass in a constant $s$ every time).

The authors do not describe how BPD/Perplexity are computed. Since there appears to be an additional variable to marginalize out (the noise schedule), these details are important and need to be explained and justified.

Practically speaking, the field seems to be moving away from discrete diffusion models and more towards discrete flow matching. The latter has a much simpler objective function and training procedure while improving results. However, I am very sympathetic to the fact that field is moving so quickly and therefore do not penalize the authors for this. However, any more discussion about how this can be extended to flow-matching would be welcome and it seems like a straightforward extension?

The writing and presentation could be improved for more clarity. There were a few instances where the writing was too imprecise for me to understand what was meant. For example, around lines 235-236, the authors write "...define pr(x_t^d) as the last event in dimension d...". It was not clear to me what is meant by and "event" and what "last" is referring to. I think what is meant is pr(x_t^d) is the state of x_t before the last noise event?

Another place where the writing could have been more clear is in the "Efficient Loss" section when the authors say "... and then add a weight representing how likely an event is to occur at the instant t." Here I think it would be helpful to write what the term is as I was left confused about which terms in Equation 5 were the weight. I believe the weight term is both the term involving Betas and the multiplication of s_t. As a reader, I was expecting this to be more clearly laid out for me.

### Questions
1) Can the authors clarify my point about masking diffusion models not having knowledge of when corruptions occur?

2) Why were experiments done with B=128 and B=256? Was is due to the fact that only for B=128 did SCUD outperform masking?
     
3) Why were different training data used in the baselines? 

4) How were the metrics computed? Specifically, how did the authors handle marginalizing the noise schedule?

### Soundness
2

### Presentation
2

### Contribution
2
