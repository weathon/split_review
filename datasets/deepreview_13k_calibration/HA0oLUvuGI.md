# Energy-Weighted Flow Matching for Offline Reinforcement Learning

- Decision: Accept
- Avg Score: 6.25
- Scores: 5, 8, 6, 6

## Abstract
This paper investigates energy guidance in generative modeling, where the target distribution is defined as $q(\mathbf x) \propto p(\mathbf x)\exp(-\beta \mathcal E(\mathbf x))$, with $p(\mathbf x)$ being the data distribution and $\mathcal E(\mathbf x)$ as the energy function. To comply with energy guidance, existing methods often require auxiliary procedures to learn intermediate guidance during the diffusion process. To overcome this limitation, we explore energy-guided flow matching, a generalized form of the diffusion process. We introduce energy-weighted flow matching (EFM), a method that directly learns the energy-guided flow without the need for auxiliary models. Theoretical analysis shows that energy-weighted flow matching accurately captures the guided flow. Additionally, we extend this methodology to energy-weighted diffusion models and apply it to offline reinforcement learning (RL) by proposing the Q-weighted Iterative Policy Optimization (QIPO). Empirically, we demonstrate that the proposed QIPO algorithm improves performance in offline RL tasks. Notably, our algorithm is the first energy-guided diffusion model that operates independently of auxiliary models and the first exact energy-guided flow matching model in the literature.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper introduces the energy-based flow matching to offline reinforcement learning without the need for auxiliary models, and then propose a novel method called Q-weighted Iterative Policy Optimization based on this framework.

### Strengths
1.	The manuscript is generally well-written and well-organized.
2.	The paper presents comprehensive theoretical proof.

### Weaknesses
1. In the reviewer’s opinion, the authors missed some existing works including EDP, and QVPO [1, 2], which also train the diffusion policy with the weighted loss. In that case, the paper does not propose anything particularly novel.
2. Given weakness 1, the authors overclaim their contribution: “Our algorithm is the first energy-guided diffusion model that operates independently of auxiliary models and the first exact energy-guided flow matching model in the literature”.
3. The reviewer thinks the proposed method should not be viewed as an energy-guided diffusion model but as an extension of RWR (reward-weighted regression) [3] via flow matching. The core idea of weighting the loss by a function of the Q-value is not new, and the authors' specific weighting scheme, which includes a normalization term, might be detrimental to learning by diluting the importance of high-Q states.
4. Results in Table 2 does not show a distinct superiority of the proposed QIPO compared with previous methods.
5. The motivation for applying flow matching to offline RL is not clear. It seems the multimodality of diffusion policy cannot be obviously improved with flow matching loss compared with normal diffusion loss.

### Questions
1.	What is the motivation of applying flow matching to offline RL?
2.	Compared with the previous works for diffusion policy with weighted loss, what is the real contribution of this paper?

### Soundness
3

### Presentation
3

### Contribution
1

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper proposes a training scheme for energy-guided continuous generative models, i.e. models that learn $q(x)\propto p(x)\exp(-E(x))$. To do so it leverages something akin to the $x_0$-conditional trick of Lipman to rewrite a loss that would depend on an intermediate energy $E(x_t)$ as simply depending on $E(x_0)$. Functionally, this is essentially a softmax-of-energy weighted loss for both flow matching and score matching models. This provably converges in the limit to an unbiased model that, unlike prior work, does not require a second model to learn a guidance.

The authors demonstrate their method on simple demonstrative tasks and a set of benchmark offline-RL continuous control tasks, where the method performs on-par with state of the art methods.

### Strengths
The paper proposes a novel solution to a very important problem, and the solution itself is fairly elegant (as most unbiased methods are in this reviewer's opinion). The paper was easy to read and used an appropriate level of detail to explain and illustrate the method. The empirical work also shows good performance on non-trivial problems.

### Weaknesses
The main weakness of the paper is it doesn't really go into the weeds of the method. Unbiased methods are great, but sometimes they come at a cost. For example, importance sampling methods are commonly thought of as high variance. It's not clear if this is the case here, or more generally what are the trade offs that would inform choosing this method over others. 

I know it's easy to write this, but there could be more empirical work done. Specifically, two very common class of problems for which these methods are used are missing, image generation and physics problems (e.g. 3d molecular conformer generation). RL is a challenging problem but the method is much more general than that, and so it feels like a missed opportunity that results on these other problems are not presented.

### Questions
One of the assumptions made seems to be that there is a prior (data distribution) $p_0(x_0)$ we can sample from, but results will differ greatly if $p_0$ is an actual sampler (e.g. a pretrained model) or a dataset (in which case you'll get some peaky behaviors). It would be good for the authors to expand on this empirically.

Relatedly, this method depends on a softmax of a potentially peaky value to learn with an off-policy objective. If the prior is flat enough and the energy peaky enough, this may very well mean that most of the data is effectively thrown away and most compute wasted because its weight is 0. There are other methods (although the ones I think of would count as concurrent work, so I'm not holding it against the authors) that learn similar amortized inference policies $q \propto p(x) \exp(-\beta E[x])$ that are able to sample on-$q$-policy (some are also able to do both off-policy and on-policy), therefore potentially wasting less data. Again not holding it against the authors to compare to those methods, but I'd love to see a deeper empirical analysis of when the proposed method works with respect to different energy landscapes; this could inform someone picking a method for their problem (and it is likely that the proposed method would be a top choice for certain problems, but not others).

Finally, I wonder what is the effect of estimating an expectation with a minibatch rather than a more precise method. For example, in the offline RL case, assuming all trajectories in the dataset come from the same policy $\mu$, then it would be much more precise to estimate $\mathbb{E}_\mu[Q^\psi]$ once over the dataset (especially if $\psi$ rarely changes), but maybe this doesn't change much.

### Soundness
4

### Presentation
3

### Contribution
4

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper presents a novel diffusion method combined with offline RL. The major contribution is that it combines flow matching loss with an energy function, specifically weighting the flow matching term with the regularized energy, which avoids calculating the gradient of the intermediate energy function. This idea is integrated into offline RL, leading to the development of Q-weighted iterative policy optimization (QIPO) with two variant velocity fields, OT and VP-SDE. Experiments on toy examples reveal the effectiveness of ED and QIPO on D4RL datasets compared to SOTA methods.

### Strengths
1. The authors provide substantial theoretical analysis.

2. The experiments reveal that QIPO-Diff and QIPO-OT outperform current SOTA offline RL methods.

### Weaknesses
1.The authors should discuss more details on the benefits of QIPO. The current methods only discuss the advantage of ED and CED over CEP, which is mainly about the diffusion models. It seems that the advantage of QIPO over other offline RL methods (e.g., SRPO, SfBC) is missing.


2. Only toy experiments on ED are given. If the authors want to claim the advantages of ED and CED, more experiments should be included, e.g., image synthesis tasks on ImageNet. I understand that verification of the diffusion model in different tasks might not be a major topic in this paper, but in its current form, QIPO appears to be a direct application of ED in the offline RL setting due to ED's advantages. Thus, empirical verification of ED is important.


3. The theoretical analysis should add more details and fix typos, e.g., in Eq. (a.5), how the div operator is eliminated should be discussed in detail.

### Questions
Please answer my questions mentioned above.

### Soundness
2

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
This manuscript discussed how to estimate the score function with an energy guidance without axillary model but can still maintain the exact guidance. The main idea is decomposing the supervision from the data population and energy guidance. The authors also extended the proposed methods to KL-regularized offline reinforcement learning.

### Strengths
* The derivations are sound and the final algorithm is intuitive.

### Weaknesses
* The presentation is not so straightforward.
* If I understand the proposal correctly, for each $\beta$ the proposed method needs to at least fine tune the score function and do the sampling. I don’t think it will have significant benefits on we directly estimate the score function without leveraging the proposed methods.

### Questions
* Will Monte-Carlo estimation on the denominator lead to a high variance on the loss/gradient estimator? It would be generally not a good idea to do something like this.
* Do CG/CFG and CEP/proposed methods only differ from the diffusion path and do we have an understanding on why this two diffusion path will lead to different empirical results?

### Soundness
3

### Presentation
2

### Contribution
2
