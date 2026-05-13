# Unremovable Watermarks for Open-Source Language Models

- Decision: Reject
- Scores: 3, 3, 3, 6

## Abstract
The recent explosion of high-quality language models has necessitated new methods for identifying AI-generated text.
Watermarking is a leading solution and could prove to be an essential tool in the age of generative AI.
Existing approaches embed watermarks at inference and crucially rely on the large language model (LLM) specification and parameters being secret, which makes them inapplicable to the open-source setting. 
In this work, we introduce the first watermarking scheme for open-source LLMs.
Our scheme works by modifying the parameters of the model, but the watermark can be detected from just the outputs of the model.
Perhaps surprisingly, we prove that our watermarks are \emph{unremovable} under certain assumptions about the adversary's knowledge.
To demonstrate the behavior of our construction under concrete parameter instantiations, we present experimental results with OPT-6.7B and OPT-1.3B.
We demonstrate robustness to both token substitution and perturbation of the model parameters.
We find that the stronger of these attacks, the model-perturbation attack, requires deteriorating the quality score to 0 out of 100 in order to bring the detection rate down to 50\%.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The paper focuses on the problem of LLM watermarking and proposes a scheme applicable to open-source models. The key claimed advantage of the scheme is its provable unremovability which the authors rigorously derive. Experimental results on two OPT models are shown, including the evaluation of robustness to token substitution and Gaussian perturbations to model weights.

### Strengths
- As the authors recognize, watermarking of open-source LLMs is one of the most important open problems in current generative model watermarking research, so studying it has the potential for high impact.

### Weaknesses
Unfortunately I believe the paper in its current state is far from being able to deliver that impact. Namely: 
- While I agree that some definition must exist, formalizing "LLM that produces high-quality text" as "closeness to the original LLM in weights of the last bias layer" seems arbitrary and far from realistic notions of quality. This greatly simplifies the problem, unfortunately making the theoretical results (claimed key contribution) largely not relevant. While I appreciate the rigor and work authors have put in proving the results, formalizing the intuition that a random vector in N-dimensional space is unlikely to match a particular unknown direction, I unfortunately do not think this provides any valuable insight in terms of the robustness of an OSS watermark to realistic transformations.
- Given this, the blanket claims that the watermark is "unremovable" (title, abstract, introduction) render as dangerous overclaims that may cause confusion in the field if the paper is accepted. These should be greatly adjusted and qualified to explain the peculiar definition of quality. To actually get a meaningful notion of unremovability, the authors could consider realistic transformations commonly applied to OSS models such as finetuning, PEFT, quantization, pruning, or at least random modification of all weights (the argument on L129/130 is unclear). These are currently neither discussed in theory nor included in the evaluation. Interestingly, the authors recognize that prior work Gu et al. (2024) considers fine-tuning yet do not consider this themselves. 
- As the authors also recognize, the proposed scheme is a variant of UnigramWatermark. While scheme simplicity is not a weakness per se, interesting/novel technical aspects of the proposed scheme are also not a strength of this paper. This is further harmed by the fact that popular LLMs often do not use the final layer bias, making the proposed scheme inapplicable. In fact, this is true for OPT models used in this work (https://github.com/huggingface/transformers/blob/v4.46.0/src/transformers/models/opt/modeling_opt.py#L1052), bringing into question the current evaluation. 
- LLM watermarking, which this paper positions itself as part of, generally focuses on detecting LLM-generated outputs. Yet, this paper starts from the related but different notion of detecting that a model was based on a watermarked model from its weights, and prove key results in this case. This is a new scenario which is unexplained and unmotivated, should be explicitly separated from the common understanding of LLM watermarking promised in early parts of the paper, and raises many questions. For example, if we assume transformations of our OSS model change nothing but the final bias layer, can't we use the other (unchanged) weights to demonstrate that the resulting model was made from our model?
- Evaluation has many drawbacks, among else it does not include any baseline (such as Gu et al. (2024)), uses high FPRs, and uses no realistic attacks on text such as paraphrasing, generally used in prior work. As the authors note, the performance of the watermark is below non-OSS baselines, which is to be expected, but does not present a case for this method as useful beyond the OSS case.
- The paper is written and presented in a confusing and convoluted way, seems to be written in a rush, and it is often very hard to understand the key parts. I include some examples/suggestions below, in hopes that this helps the authors get insight into the issues and improve their writing in the future to the level expected at ICLR. I am happy to further assist the authors here if they have questions. 
- (Minor) While this does not affect my assessment, L173 contains another dangerous claim, citing Zhang et al. (2024) to say that any LLM watermark is removable. This is a misunderstanding of the original paper which studies an idealized case where a random walk on the space of "equivalent" documents is possible while preserving quality, and the random walk is rapidly mixing. To avoid misinforming readers, this citation should be appropriately qualified.

### Questions
- In Theorem 1 shouldn't the distribution over $w^\star$ be centered at $w_{wat}$ and not 0? This is also present in the proof and Theorem 3. Is this a mistake or my misunderstanding of the statements?
- L145 states that Aaronson (2022), Christ (2024) and Fairoze (2023) are based on partitioning the tokens into red and green lists. Can you elaborate on this view of these methods, as my understanding was that they are quite different and do not use the red/green concept? 
- Were OPT models modified to use the final layer bias to enable experimental evaluation?

### Soundness
2

### Presentation
1

### Contribution
1

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper proposes a method for embedding watermarks in large language models (LLMs). This method incorporates watermark information by adding noise that follows a normal distribution to the model's output, with the noise serving as the watermark's key. The authors also demonstrate that, under certain assumptions, the embedded watermark is unremovable. The feasibility of the proposed scheme is validated using the OPT-6.7B and OPT-1.3B models.

### Strengths
1. The authors attempt to embed noise information following a normal distribution as a watermark into the text output of the model. This is an interesting endeavor that could potentially aid future watermark embedding algorithms.

2.The paper attempts to theoretically discuss the unremovability of watermarks, which is also an interesting analysis.

### Weaknesses
 - Now, the authors claim to have introduced the first watermarking scheme for open-source LLMs. What do they mean by this? There are many watermarking schemes which could be deployed in open source LLMs, so this claim might not be right, as the proposed scheme can also be deployed in closed source LLMs by the model owners. Which leads to the next question. If the LLM is open source, what exactly is the benefit of watermarking when the attacker has direct access to model's weights. Can the authors expand more on their motivation?
- The proposed approach embeds watermark signals to the bias of the last layer's neurons. There is another approach by ByteDance that injects watermark into the LLM weights by finetuning (https://arxiv.org/pdf/2403.10553). Why is there no comparison with this approach? Infact, why is there no comparison with other watermarking schemes at all?
- There are adaptive ways to bypass watermarks. One is by using adaptive paraphrasers. If the proposed watermark scheme is unremovable, yet detectable, why are there no empirical results proving the 'unremovability' claim using adaptive paraphrasers, or even normal paraphrasers like Dipper, or even using open source LLMs for paraphrasing.
- How efficient is the detection process? How many tokens does it require to detect the proposed scheme, especially using its optimal hyperparameters? I feel the experiments the authors provided to prove the efficiency and strength of this approach are not enough.

### Questions
1. What is the relationship between Algorithm 4 and Algorithm 3? If Algorithm 4 is the primary method for text watermark detection, then when is Algorithm 3 invoked?

2. How is the symbol \Delta (x_i) defined in Algorithm 4? How is it calculated? 

3. In watermark detection, each token should be evaluated. Why is it necessary to check x_i \in S in line 4 of Algorithm 4?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper introduces the first watermarking scheme for open-source LLMs. The idea is to embed a watermark directly in the model's parameters rather than through the sampling algorithm, making it resilient to tampering in open-source environments. The authors define "unremovable watermarks" for neural networks and implement a scheme that perturbs neuron biases in the model's final layer with Gaussian noise. Detection of the watermark is achieved either by examining the weights for specific bias patterns or by analyzing output text for token frequency markers. The watermark is shown to be unremovable, as attempts to erase it degrade model quality, with experimental results on OPT-6.7B and OPT-1.3B supporting this claim.

### Strengths
- The paper introduces a new watermarking scheme to embed unremovable watermarks directly in model weights and resist tampering in open-source environments.
- The paper defines "unremovable watermarks," providing proofs and an analysis of the watermark’s robustness against attacks and conducting experiments with OPT-6.7B and OPT-1.3B models to demonstrate the approach's effectiveness.
- The paper is well-structured, logically presenting its motivation, methodology, and findings, with clear definitions and algorithms. I highly commend the authors for the nice presentation.

### Weaknesses
The paper does not fully address several, by now well-recognized aspects, of the watermark:
1. Robustness of the watermarks. E.g., what if one changes even two characters of the produced output? Or that it deletes parts of the output. Here the paper claims it has done experiments but i could not figure out what exact perturbation channels are studied.
2. It seems that the output of the watermarked model here is *not* indistinguishable -- sometimes called undetectable or distortion free -- (in comparison with non-watermarked model's output). This is the ultimate way of arguing that the model’s utility does not degrade after adding the watermark and the paper does not discuss it clearly. Note that here, I am not talking about "removability". This is about the item above (robustness) but rather if the output of the watermarked model differs (in a computationally noticeable way) from the output of non-watermarked model.

To partially address the above issues, the paper should first define clearly what class of perturbation channels they study (and why they are interesting) for the robustness property evolutions (which are seemingly done under the name of Detectability) and for the item 2 above (undetectability of the output -- which is different from the Detectability study) they should design experiments specifically for this goal or make a theoretical assertion.

Also, the proofs are based on multiple assumptions, which make the final conclusion far from ideal. (See my question below)

Also, what happens to the watermarks if the model is fine tuned? (note that black-box methods still work, if the model is fine tuned). This issue should be addressed using experiments. they could be simple experiments that simply test the detectability and utility of the outputs after a fine tuning for specific goals (also see my question below).

The writing also is not great and lacks discussions and justifications with regard to the issue mentioned above (e.g., of the assumptions).
Other than the issues above, the intuition behind why this non-black-box approach is working could be much better.

Other minor comments on writing:

Def 2 seems to be more like a “similarity” measure, because the loss in quality seems to be different. For example, two models could look very different but have the same quality of responses.

Def 4: seems to mix the input space of Q and \ell, right?

### Questions
Please answer those in weaknesses above.

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The problem of watermarking the output of LLMs has been around for some time. Previous work has focused on changing the output distribution of the LLMs, sometimes in an “undetectable/distortion-free” way. But this work starts by making the following point:
If one has access to the parameters of an LLM, they can run it to generate output that is not watermarked. 

The main problem of this paper is to watermark the parameters of the model itself, in a way that it both gets reflected in the output + even if one gets their hand on the model parameters, they cannot modify it in a way that the watermark is removed from subsequent outputs.

Of course one shall consider attackers who can train the model from scratch. So the paper assumes that doing so is hard (e.g., by making the access to the data generation process costly).

The contribution of the paper is the following. They propose a scheme that works by adding Gaussian noise to the last layer of the model before publishing it. Also knowing the original model and the noise, they show how to verify whether the generated output comes from their model or not.

The paper then makes multiple assumptions to prove that their scheme is secure. The final watermark suffers from not having robustness or undetectability. It is not clear if such weaknesses are inherent or not.

### Strengths
As far as I know, this is the first work that aims to formally define and address “unremovable watermarks” that are planted in open source models.

### Weaknesses
The paper does not fully address several, by now well-recognized aspects, of the watermark:
1. Robustness of the watermarks. E.g., what if one changes even two characters of the produced output? Or that it deletes parts of the output. Here the paper claims it has done experiments but i could not figure out what exact perturbation channels are studied.
2. It seems that the output of the watermarked model here is *not* indistinguishable -- sometimes called undetectable or distortion free -- (in comparison with non-watermarked model's output). This is the ultimate way of arguing that the model’s utility does not degrade after adding the watermark and the paper does not discuss it clearly. Note that here, I am not talking about "removability". This is about the item above (robustness) but rather if the output of the watermarked model differs (in a computationally noticeable way) from the output of non-watermarked model.

To partially address the above issues, the paper should first define clearly what class of perturbation channels they study (and why they are interesting) for the robustness property evolutions (which are seemingly done under the name of Detectability) and for the item 2 above (undetectability of the output -- which is different from the Detectability study) they should design experiments specifically for this goal or make a theoretical assertion.

Also, the proofs are based on multiple assumptions, which make the final conclusion far from ideal. (See my question below)

Also, what happens to the watermarks if the model is fine tuned? (note that black-box methods still work, if the model is fine tuned). This issue should be addressed using experiments. they could be simple experiments that simply test the detectability and utility of the outputs after a fine tuning for specific goals (also see my question below).

The writing also is not great and lacks discussions and justifications with regard to the issue mentioned above (e.g., of the assumptions). 
Other than the issues above, the intuition behind why this non-black-box approach is working could be much better.

Other minor comments on writing:

Def 2 seems to be more like a “similarity” measure, because the loss in quality seems to be different. For example, two models could look very different but have the same quality of responses.

Def 4: seems to mix the input space of Q and \ell, right?

### Questions
Can you address the two issues of robustness (to small change in the output) and the undetectability of the output (compared to the non-watermarked model) ?

 In your experiments, how do you measure that the utility of the model has not degraded after adding the watermark. I know that you have an oracle that measures the degrading, but then you instantiate the oracle using mathematical formulas regarding the model. But how do you make sure that this reflects the actual quality of the model’s output? For example, you could use specific metrics or human evaluation methods to assess output quality more directly.

Can you discuss why the assumptions are fine? There are 3 explicit assumptions and (multiple) implicit assumptions in the statement of Theorem 1 (eg., “let C be such that…” or “c_2-high quality…”) I think that discussion is needed before calling assumptions reasonable (instead of putting the word reasonable in the theorem statement).

Can you argue either way about the effect of fine tuning in your watermarked model?

In your experiments: can you be more explicit about what your attacker is? e.g., using a pseudocode.

### Soundness
2

### Presentation
2

### Contribution
2
