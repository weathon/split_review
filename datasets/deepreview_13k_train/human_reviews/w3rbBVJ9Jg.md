# PIMRL: Physics-Informed Multi-Scale Recurrent Learning for Spatiotemporal Prediction

- Decision: Reject
- Scores: 8, 5, 6, 6

## Abstract
Simulation of spatiotemporal systems governed by partial differential equations is widely applied in fields such as biology, chemistry, aerospace dynamics, and meteorology. Traditional numerical methods incur high computational costs due to the requirement of small time steps for accurate predictions. While machine learning has reduced these costs, long-term predictions remain challenged by error accumulation, particularly in scenarios with insufficient data or varying time scales, where stability and accuracy are compromised. Existing methods often neglect the effective utilization of multi-scale data, leading to suboptimal robustness in predictions. To address these issues, we propose a novel multi-scale learning framework, namely, the Physics-Informed Multi-Scale Recurrent Learning (PIMRL), to effectively leverage multi-scale data for spatiotemporal dynamics prediction. The PIMRL framework comprises two modules: the micro-scale module embeds physical knowledge into neural networks via pretraining, and the macro-scale module adopts a data-driven approach to learn the temporal evolution of physics in the latent space. Experimental results demonstrate that the PIMRL framework consistently achieves state-of-the-art performance across five benchmark datasets ranging from one to three dimensions, showing average improvements of over 9\% in both RMSE and MAE evaluation metrics, with maximum enhancements reaching up to 80\%.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper introduces physics informed multi-scale recurrent learning (PIMRL), which is a novel architecture for learning both micro and macro time scales commonly present in real world data. Specifically, PIMRL introduces a micro and macro architecture, along with corresponding training schemes, that provides an implicit bias for the network to learn both micro and macro timescales.


# Post rebuttal

The authors did a great job addressing my concerns. As such, I am raising my score.

### Strengths
I want to preface this by saying that I'm not an expert in PDEs nor in deep-learning based approaches for solving PDEs. Nonetheless, I am a big fan of the proposed approach. The proposed architecture is something I have never seen before and is very nifty! I am also very impressed by the experiments section! Specifically, I LOVE that the authors look at multiple different metrics which allows one to look at the results from multiple different angles, which is very important.

### Weaknesses
I want to preface this section by saying that I am not an expert in this field. I hope that a non-expert's viewpoint will provide criticism that will make this paper stronger.

There are two big weaknesses that I think limit the paper from being truly great. The first is the writing. There are A LOT of interesting things in this paper that are not adequately explained nor properly described. Moreover, there is a lot of text and figures that are confusing and don't add much to the text; they could be removed to allow for the other aspects of the paper to shine. I will list my qualms with the writing below

- To start, the authors begin by stating that "direct numerical simulation requires a deep understanding of physics" but it is not clear what this means. Do the authors mean that one needs an understanding of physics to come up with PDEs that describe physical phenomena? This is independent of numerical simulating equations as a solver does not need to know what physical phenomena an equation is trying to describe. Moreover, since the name of the proposed approach is physics-informed multi-scale recurrent learning, does this not imply that a deep understanding of physics would also be required to effectively use PIMRL?

- Next, Figure 1 takes up a lot of space but does not add much. Personally, given its vagueness it confused me on what PIMRL is. Figure 2 does a much better job explaining the method. I would recommend removing figure 1.

- A big part of PIMRL is PerCNN, as the micro-scale architecture is exactly the PerCNN architecture. To me this is not an issue as science is built upon previous works, but I would have preferred the authors explicitly stated this, i.e., 'We introduce PIMRL, which combines the micro-scale power of PerCNN, with a novel macro scale architecture to..." Next, it is also not clear why PerCNN needed an extension in the first place (this evidence is lacking both in the text and in the experiments section). In the related works section, the authors state the following about PerCNN "However, the model suffers from error accumulation during long rollout predictions. To address this issue, a straightforward approach is to reduce the frequency of iterations by increasing the time stepping. Nonetheless, for hard-embedded methods like PeRCNN, accuracy is limited by the time stepping, making simple modifications unfeasible". This doesn't make any sense to me. In PerCNN, one can choose both the number of iterations in a the $\Pi$ block as well as the time step, $\delta t$; thus, it seems it would be rather straightforward to train PerCNN on macro-scale data. Moreover, the comparison to PerCNN doesn't seem fair. First, similar to what the authors did for FNO, it seems straight forward to also include a PerCNN coarse and fine scale. One could even just train one PerCNN on both the micro and macro scale data, where $k$ is dataset dependent. 

- To me the most interesting part of the approach is how the macro and micro modules interact. Sadly, this is not given time to shine in the paper! For instance, why was this interaction between the macro and micro module chosen? What role does the mirco-module serve (i.e., does it serve as error correction for the initial condition?)? There are so many interesting design choices here that I think are fascinating but sadly are missing.

- In the paper, the authors use the term physical embedding where they state "... physical embedding methods, where explicit physics knowledge is embedded into the model to fully leverage physical principles...". They also state that PIMRL uses this but the entire approach is data-driven. If by physical embedding they mean the *Optional* physical-based FD conv then they should explicitly state this. Also, I think the fact this is *optional* weakens the statement considerably.


The next weakness is the experiments section. While the results are compelling and I love that they look at the results from multiple different angles, I think there are some major things missing.
- There are no details on how the datasets are constructed. What solver was used? How were the initial conditions chosen?
- The authors state that they create a micro and macro dataset for training PIMRL. For the other baselines, it seems like they were either trained on the micro or macro dataset. On a first read, it seems like PIMRL was trained on more data. Was the dataset size equalized for the baselines?
- Error bars are missing in the error propagation plots and Table 2!
- The ablation study is missing a lot of details. For instance, what does the NoConnect model mean? Is it just purely the micro module or the macro module?
- Without knowing the solver, the inference time figure is a little underwhelming.

### Questions
I think most of my questions were listed in the weakness section.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This work introduces a framework for handling multi-timescale data by modeling dynamics across two time scales. A micro module manages the high-frequency observations, while a macro module captures long-term dependencies. The micro module operates directly on physical states, leveraging PerCNN, whereas the macro module learns in a latent space and uses a ConvLSTM block for temporal propagation. Initially, the micro module is pretrained, and later fine-tuned jointly with the macro module using mean-squared error (MSE) supervision. The experiments appear to yield promising results.

### Strengths
The paper presents a clear and well-formulated motivation that connects nicely with existing literature.
Experimental results are well-discussed and appear conclusive, demonstrating notable improvements over comparable methods.

### Weaknesses
 - The model seems to require aligned micro- and macro-scale training data, which may limit its applicability.
- While the model presentation is well-structured, its technical novelty is somewhat limited, as it could be considered a specific implementation of Rubanova et al. [1]. The core idea of using a micro-module for short-term dynamics and a macro-module for long-term dependencies, while intuitive, lacks a significant departure from existing approaches. The specific implementation details, such as the use of PerCNN and ConvLSTM, are well-established techniques in the field, and their combination, while effective, does not introduce a fundamentally new concept. The message-passing mechanism, while presented as a key contribution, appears to be a specific configuration of existing temporal propagation methods, making the overall novelty incremental rather than transformative.

Would the authors consider working with unaligned datasets, such as those with only micro-scale or only macro-scale trajectories?

### Questions
1. Despite Figure 2, it remains challenging to understand the inference process. I suggest clarifying the figure or including a detailed description in the manuscript.
2. Is the RMSE computation performed on the micro- or macro-scale data?
3. Is model training robust to the number of training trajectories? Exploring the model’s scalability in relation to both the micro and macro modules would be insightful.
4. Does the model require consistency in the underlying physical parameters during training ? said otherwise, is it robust to out of distribution trajectories ?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces a data-driven model to simulate a spatiotemporal system. It proposes to leverage multi-scale data by embedding physical knowledge into a micro-scale module and employing a data-driven approach for its macro-scale module. 
The method is then tested on various fluid dynamics and reaction-diffusion systems equations, reaching impressive results on a challenging dataset.

### Strengths
- the paper is beautifully illustrated, making the methods easy to read understand and the results easy to read and understand
- the proposed method outperforms the state of art on a variety of PDEs

### Weaknesses
 - Some method details lack clarity, especially regarding the physics operator. Specifically, the paper does not clearly define how the physics-based convolutional layers are constructed or how the finite difference stencils are chosen for different PDEs. The description lacks the necessary detail for reproducibility, making it difficult to understand the exact implementation of this crucial component.
- the related work and baselines seem to lack a few strong methods. For example, there is extensive literature on improving FNO (including some published here last year: [https://openreview.net/pdf?id=tmIiMPl4IPa]. Is there a reason for using FNO and not its extensions? 
[https://arxiv.org/abs/2204.11127] also seems a like a strong baseline. The paper should include a more comprehensive comparison with state-of-the-art methods, particularly those that build upon the FNO architecture, to better contextualize the performance of the proposed approach.
- The ablation study lacks depth: more details on each module's contribution, the micro-scale module's pre-training, and some parameters would help understand the contribution of the method. The ablation study should include a more granular analysis of the impact of each module, including the physics-based convolutional layers and the $\Pi$-block. Furthermore, the pre-training procedure for the micro-scale module should be detailed, along with the sensitivity of the model to different hyperparameter settings.

### Questions
- It is not clear how the boundary conditions are encoded in each baseline: is boundary padding also used? If not it seems like an unfair advantage as it has access to additional information
- why is the Physics operator optional? Does it depend on the dataset? If not, it should be added to the ablation study.

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
5

### Summary
This paper focuses on the temporal multi-scale property of spatiotemporal systems and proposes a multiscale recurrent learning framework, named PIMRL. In this model, the micro-scale module learns to embed multiscale data and the macro-scale module captures the data-driven evolution. PIMRL performs well in five different tasks.

After rebuttal: I think most of my concerns have been resolved. Thus, I have raised my score to 6 and changed the score of presentation and soundness.

### Strengths
This paper focuses on an important problem: the temporal multiscale property, which is mainly overlooked in previous methods.

The experiments are relatively comprehensive. The authors test PIMRL in five typical tasks.

### Weaknesses
1.	About the writing.

I believe that this paper needs a significant revision to ensure a clear presentation. Here are some examples.

(1)	Introduction: There are many important concepts without explanation. For instance, the authors claim that the micro-scale is “pretrained” in the abstract and introduction. However, in the method part, there are no descriptions of how this pretraining be implemented.

(2)	Related work: The authors fail to provide a clear organization of the related work. For example, ConvLSTM is just one classical (maybe old) baseline in spatiotemporal learning. There are extensive papers that weren’t included, such as PredRNN [1] or TrajGRU [2].

(3)	Method: I think Eq. (2) and (3) do not provide a clear and right formalization for the overall framework. The descriptions of the prediction protocol are self-contradictory. Given that each micro module can conduct a \delta t stepsize transition and the macro module is \Delta t, why the output of Eq.(3) is just t+k\delta t. Besides, as they presented in Figure 2, I cannot tell which part is “history information” or if the micro-scale module is applied to the model prediction or not. A flowchart or pseudocode can be helpful.

The low quality of writing seriously affects the contribution of this paper.

2.	Compare with more advanced baselines.

As the authors mentioned in Lines 125-133, there are many advanced Neural Operators such as MWT and U-NO, which should be compared.

3.	About the novelty.

As the proposed method is more like a multiscale ensemble method, I cannot score high for the novelty.

### Questions
Why did the authors name the micro module as “physics-informed”? Actually, I think the formalization of Eq. (4) is just a convolution neural work, which is far away from the conventional definition of “physics-informed neural networks”.

### Soundness
3

### Presentation
2

### Contribution
2
