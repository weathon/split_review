# Predicting the Energy Landscape of Stochastic Dynamical System via  Physics-informed Self-supervised Learning

- Decision: Accept
- Avg Score: 5.75
- Scores: 6, 5, 6, 6

## Abstract
Energy landscapes play a crucial role in shaping dynamics of many real-world complex systems. System evolution is often modeled as particles moving on a landscape under the combined effect of energy-driven drift and noise-induced diffusion, where the energy governs the long-term motion of the particles. Estimating the energy landscape of a system has been a longstanding interdisciplinary challenge, hindered by the high operational costs or the difficulty of obtaining supervisory signals. Therefore, the question of how to infer the energy landscape in the absence of true energy values is critical. In this paper, we propose a physics-informed self-supervised learning method to learn the energy landscape from the evolution trajectories of the system. It first maps the system state from the observation space to a discrete landscape space by an adaptive codebook, and then explicitly integrates energy into the graph neural Fokker-Planck equation, enabling the joint learning of energy estimation and evolution prediction. Experimental results across interdisciplinary systems demonstrate that our estimated energy has a correlation coefficient above 0.9 with the ground truth, and evolution prediction accuracy exceeds the baseline by an average of 17.65\%. The code is available in the anonymous repository: https://anonymous.4open.science/r/PESLA-0D9A/README.md

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes to infer the energy landscape of complex, stochastic dynamical systems. A distinguishing feature is the adoption of vector quantization techniques for dimension reduction. Dynamical information was inferred via a graph neural Fokker-Planck equation method. A regularization term was introduced to constrain the long-term prediction behavior between the empirical distribution p and the Boltzmann distribution. The novelty of bringing together these ideas is appreciated. Experiments were performed on 3 tests: 2d Prinz potential, ecological evolution, and fast-folding peptides. The method part of the paper is not very clear and somewhat difficult to follow. There is no ablation tests, so it's hard to see what the various loss terms or model designs offer. There is no discussion of the limitations of the method.

### Strengths
The idea of bringing together several novel methods for modeling stochastic dynamical systems is very interesting. Three different examples cover different application areas and add to the credibility of the method. The capability to learn unknown energy landscape from stochastic dynamical systems is a potentially high-impact contribution.

### Weaknesses
The description of the overall model is not clear to me. At least not easy to follow. For example, the encoder, decoder, Phi, Psi, Xi,... were defined in different places and some were not clearly defined. What space and dimension does Phi map from and to? Please make it easier to follow. And the dimension of latents such as H is not clear. Please collect the equations in a coherent way, e.g. all the different losses, and what are the losses sampled over?

Overall, the writing of the paper is too hand-waving. As a referee I don't like guesswork.

There is no ablation tests, so it's hard to see what the various loss terms or model designs offer.

There is no discussion of the limitations of the method.

Consider adding some explanation of the graph FPE method. FPE models the evolution of the probability p, not its encoding Phi(p) as in eq (4). I suppose it is explained in the cited reference. But since it is a central piece of this paper, please explain how this works.

### Questions
* Please discuss the issue of transferrability. Can the trained model be transferred to unseen structures? Was a separate model trained for each protein? Which of the sub-modules, encoder, decoder, etc, can be reused?

* Scalability. To model a bigger protein, how large does the codebook need to be? What about training and inference cost for longer sequences?

* Spell out KNN (k-nearest neighbor?)

* How are encoder Ξ, decoder Ω implemented? GCNN was mentioned but I still have no idea what's in the model.

* There is no ablation tests, so it's hard to see what the various loss terms or model designs offer. 

* There is no discussion of the limitations of the method.

* Consider adding some explanation of the graph FPE method. FPE models the evolution of the probability p, not its encoding Phi(p) as in eq (4). I suppose it is explained in the cited reference. But since it is a central piece of this paper, please explain how this works.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The authors propose an algorithm for discovering the energy function that may explain data trajectories assumed to be driven by the gradient of the energy plus noise. Their model learns a partitioning of the space with one discrete symbol per region and an associated energy value, along with a decoder (and associated encoder) mapping to the observed continuous space. They assume that the dynamics is driven by the energy difference between nearby partitions and Markovian transitions between regions. The model is evaluated on three tasks and compared with several baselines.

### Strengths
This is an interesting learning problem, also requiring to learn a latent explanatory space for sampled continuous time trajectories. The authors compare against multiple baselines across everal environments. The results appear encouraging.

### Weaknesses
(1) I do not see how such an approach can generalize outside of the visited regions, i.e., the cluster centers corresponding to the codebook entries; in general, the most interesting energy functions can have a very large (if not exponential) number of energy wells, and one needs to generalize from the visited wells to new ones. The reason is that many factors may be composed that give rise to stable solutions. Hence a multivariate representation of the discrete identities must be constructed (think about language, which is discrete but allows generating a huge number of legal combinations of words).

(2) It is not clear to me that g in general will preserve all information about the energy of the state, so it may be necessary for the encoder (from observations to states) to look at the whole past trajectory in order to make a probabilistic guess about the state proxy.

(3) the main model (sec 3.2) is not sufficiently understandable and could use more motivation for its different parts. Why these equations in particular (4 and 5).

(4) The experimental setup seems to lack comparisons with *published results* from earlier work, which makes it difficult to know if the comparisons are fair.

(5) The test set includes only trajectories from the same system for which a training trajectory is given, i.e., there is no form of generalization to new systems (e.g., new molecules).

### Questions
* to address (3) above, please provide better justifications for the main model and the associated training losses

* to address (4) and (5), please compare with published results on recovering the energy and fitting new trajectories of new molecules or systems

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
Estimating the energy landscape is challenging because obtaining direct energy measurements is costly. To bypass this process, the paper proposes a physics-informed self-supervised learning approach, where the energy landscape is estimated from historical evolution trajectories instead of direct energy signals. This method uses discrete codebook embeddings, assuming that energy landscapes generally have low intrinsic dimensionality. Additionally, a physics-informed graph neural Fokker-Planck architecture and physics-inspired regularization are employed to predict system states more accurately.

### Strengths
The paper begins with a strong motivation, highlighting the challenges in obtaining direct energy values. Additionally, it provides a solid rationale for incorporating discrete codebook embeddings into their method, based on the inherently low dimensionality of energy landscapes.

### Weaknesses
1. The ablation studies in this paper seem too limited. Since multiple modules are introduced in their method, additional experiments are needed to clarify the individual contributions of each component to the overall performance. For instance, it would be helpful to examine the effect of using discrete versus continuous embeddings. Specifically, a comparison should be made where the continuous embeddings are also used within the same graph neural Fokker-Planck architecture, rather than switching to an RNN, to isolate the impact of the embedding type. Similarly, given that five types of losses are included, an analysis of each loss’s specific impact would provide valuable insights. For example, the effect of removing each loss term individually, and in combinations, should be explored to understand their interactions and relative importance. If these results were included, I would increase my rating.

2. Regarding  $L_{phy}$, could you explain in more detail why this loss is referred to as “physics-inspired”? How it differs from standard machine learning loss terms?

3. There are five types of losses ( L_{reconstruct}, L_{vq}, L_{latent}, L_{code}, L_{phy}) in total. Could you clarify the exact meaning of the terms $\mathbf{p}$ and $\mathbf{q}$ in each loss?

### Questions
See Weaknesses

### Soundness
3

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
This paper proposed a new framework PESLA to estimate the energy landscapes from the evolution trajectories of the system. The framework includes two stage, first it uses an adaptive codebook to obtain a discrete landscape space from the observation trajectories. Second, it uses a graph neural ODE based on the Fokker-Planck equation to predict system evolution.

### Strengths
- The paper is clearly written. 

- The method is trained in a self-supervised manner, hence it can conduct estimation without knowing true energy landscape.

- The methods were evaluated on three interdisciplinary systems and all demonstrated an improvement compared with SOTA baselines.

### Weaknesses
 - The author mentioned that “observable evolutionary trajectories typically cover only a limited portion of the vat state space”, however, the paper did not explain how the purposed method perform in the situation when the available data is biased or very sparse. Specifically, it is unclear how the adaptive codebook handles situations where certain regions of the state space are significantly underrepresented in the training data. This could lead to inaccurate energy landscape estimations in those regions, and consequently, unreliable trajectory predictions.

- The method relies on the assumption that the system is driven by energy and a well-defined low dimensionality energy landscape exists. Therefore, the assumption might limit the applicability, which was not discussed in the paper. The paper should address the limitations of this assumption, especially when dealing with systems where non-conservative forces or time-varying landscapes play a significant role. The method's performance in such scenarios is not explored, raising concerns about its generalizability.

- The method is lack of interpretablity. The training fully relies on the final trajectory prediction errors to avoid knowing true energy landscape, however, it is not discussed how reliable or meaningful of the predicted trajectory and the estimated energy landscape. For example, dose the correlation of the estimated energy landscape and true energy landscape influence the final trajectory prediction? It is unclear how the learned latent space relates to the actual energy landscape and whether the predicted trajectories are physically meaningful or simply a result of the optimization process. The paper should provide a more detailed analysis of the interpretability of the learned representations and their connection to the underlying physics of the system.

### Questions
- What is the computational complexity of the proposed methods and its comparison to existing methods? 

- Are the estimate energy landscape consistent under different hyperparameters?

- Does the granularity of the discretization of the energy landscape influence the accuracy of system evolution estimation?

- Considering that real-world trajectory data is usually noisy and sparse, how robust is the method to such data?

### Soundness
3

### Presentation
4

### Contribution
3
