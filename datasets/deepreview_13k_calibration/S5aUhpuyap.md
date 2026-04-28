# Complex priors and flexible inference in recurrent circuits with dendritic nonlinearities

- Decision: Accept
- Avg Score: 5.75
- Scores: 6, 6, 5, 6

## Abstract
Despite many successful examples in which probabilistic inference can account for perception, we have little understanding of how the brain represents and uses structured priors that capture the complexity of natural input statistics. Here we construct a recurrent circuit model that can implicitly represent priors over latent variables, and combine them with sensory and contextual sources of information to encode task-specific posteriors. Inspired by the recent success of diffusion models as means of learning and using priors over images, our model uses dendritic nonlinearities optimized for denoising, and stochastic somatic integration with the degree of noise modulated by an oscillating global signal. Combining these elements into a recurrent network yields a stochastic dynamical system that samples from the prior at a rate prescribed by the period of the global oscillator. Additional inputs reflecting sensory or top-down contextual information alter these dynamics to generate samples from the corresponding posterior, with different input gating patterns selecting different inference tasks. We demonstrate that this architecture can sample from low dimensional nonlinear manifolds and multimodal posteriors. Overall, the model provides a new framework for circuit-level representation of probabilistic information, in a format that facilitates flexible inference.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper presents a neural circuit model for Bayesian inference, where the prior is proposed to be encoded via a DDPM-like mechanism in the dendrites of neurons. Some additional modifications were made to be more biorealistic, such as the dendrites instantiated as tree-structured MLPs, and iterative prior sampling driven by a global oscillatory noise schedule (as opposed to the standard, “discontinuous” reverse diffusion sampling). The authors show demonstrate that, on a swiss-roll toy task, the neural sampler performs similarly to the standard DDPM. Furthermore, the authors demonstrate how the prior can be flexibly combined with multiple additional sources of information (likelihoods), such as sensory observation and contextual signals, for posterior sampling. Finally, the authors make experimental predictions on how different phases of the global oscillation would be informative if such a representation is implemented in real neural circuits.

### Strengths
I found the paper to be clearly and concisely written, with very informative figures to illustrate the main idea and key results. The proposed circuit implementation of a diffusion model in the dendrites is interesting and novel, while the oscillatory noise schedule is an elegant device, with an intuitive (though potentially misleading) mapping to neural oscillations. As demonstrated, the proposed model can incorporate multiple likelihood sources separately, and at least for the toy tasks, achieve good performance. I did not examine the math thoroughly, but overall I believe the paper is of high technical quality, and presents an interesting hypothesis (and testable model) for how neural circuits may encode priors.

### Weaknesses
For me, the paper suffers from two major weaknesses:

First, while the model is elegant and combines a SOTA class of generative model in ML (DDPMs) with neural circuitry, the end product feels too artificial in construction and biologically implausible, with its many strong restrictions / assumptions. For one, the diffusion model in this implementation can be trained as per usual, but how would real dendrites in a neuron go through this learning? The authors state the the learning aspect is for future work, but that’s a huge “if”—is it really realistic to suppose that such a complex mechanism can emerge in vivo, without any hint for the readers of how it could? Additionally, sampling critically depends on a stationary and permanent oscillation, which is rarely found in the brain. Even hippocampal theta, which the authors draw inspiration from, are irregular in time and frequency, nevermind oscillations in other cortical areas.

Second, the performance is only demonstrated on a relatively simple task of sampling from a very smooth and low-dimensional manifold. I understand that the quantitative results are mostly a demonstration of proof of principle. However, there’s no indication that this would work with mildly more complex high-d distributions, as the authors had originally motivated (and pointed out as a weakness in previous literatures, i.e., mostly Gaussian prior/posteriors). It would be nice to have some indication of how this can be scaled to perform a mildly more complicated task, like conditionally sampling MNIST, or would it be completely infeasible given the architectural constraints?

These are the two major categories of concern, and I have a number of other concrete issues in the limitation / questions sections below. Taken together, I am skeptical of how much of the claims regarding “neural circuit implementation” is substantiated. And if not, how impactful would the contribution be, which is essentially connectivity-constrained DDPM with an oscillatory noise schedule. Therefore, I recommend borderline reject, noting that it is a well written paper (with some technically dense sections) and solid work but perhaps for a more niche readership, and that I am open to be convinced of its potential biological relevance.

### Questions
- is there recurrent interaction between neurons? It’s also a bit unclear how many neurons there are, or are all the results from a single dendritic tree? Also, what exactly are the inputs/outputs of the dendritic networks, and what exactly is the somatic “compartment” doing, or is that functionally just the last layer of the dendrites? Apologies if I had missed this obvious info.
- In the case of posterior inference (Figure 2/3), do the samples still show zero autocorrelation?
- I may have fundamentally misunderstood something, but the authors motivate their proposed architecture as flexible, since it can be reused for various inference scenarios, just swapping out or combining likelihoods. This is demonstrated well for the current model, but wouldn’t this be true for a model where a different population encodes the prior as well? Why is it necessary that it’s in the dendrites? Or is that just a “semantic” difference, since the branching networks can equally be implemented as different neurons?
- Isn’t it typically the case that bottom-up sensory info and contextual info are thought to be likelihood and prior, respectively? Whereas here, they are represented as two different steams of likelihoods. Can the authors comment on this discrepancy?
- there is a recent body of experimental evidence implicating oscillations of different frequencies coordinating bottom up (gamma, ~40Hz) vs. top down (beta, ~15Hz) signaling (see A. Bastos, EK Miller, etc.), while here it’s crucial that there is a global oscillation of a single frequency, otherwise the prior and likelihood sampling are temporally misaligned.
- The proposed implementation draws one prior / posterior sample per oscillation cycle, which, given the fastest cortical rhythm (40Hz gamma), results in 40 samples per second, and more likely to be less, e.g., 8Hz theta in the hippocampus. Is this sampling speed too slow? Does it match behavioral data of evidence accumulation?
- As I mentioned above, most of the time, most areas of the cortex are not experiencing oscillations. Furthermore, oscillations tend to disappear during task engagement (such as 10Hz alpha in visual areas and 20Hz beta in motor areas), which would be a time that is critical for sampling. How reliable would the proposed implementation be in such scenarios?
- caption for Figure 1F is missing

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
In this paper, the authors proposed a diffusion-based recurrent circuit for sampling-based probabilistic computation. They used recurrent circuits to represent complex priors implicitly, and the sampling-based inference was accomplished using noise modulated by an oscillatory global signal. The recurrent circuits implement the diffusion models with dendritic nonlinearities and stochastic somatic integration. They showed that the dynamics can be gated by bottom-up or top-down signals to generate samples from the corresponding posteriors in low-dimensional nonlinear manifolds and multimodal posteriors to achieve flexible inference.

### Strengths
There have been earlier works exploring ideas of recurrent connections to encode priors and the neural dynamics to perform Langevin sampling. The proposed plausible neural circuit implementation of across-task inference in which a common prior is encoded in the recurrent connections with dendritic nonlinearities optimized for denoising is novel.  The connection to diffusion models,  the use of global oscillatory signals as sampling control, and the use of bottom-up and top-down signals for gating the samplings across multiple tasks are also new and interesting and represent a conceptual advance. It does provide a new plausible framework to allow flexible sampling of complex distributions.

### Weaknesses
While the connection to DM is inspiring, there is no direct evidence to support the key assumptions and innovation of the model -- the dendritic nonlinearities and DM-inspired oscillatory sampling schedule. They remain a fragment of imagination.  As it is mostly a theoretical neuroscience model that works only on a toy example for demonstration, it would be worthwhile to articulate the predictions and the assumptions of the model that can be tested and evaluated by neurophysiological experiments. The specific form of the dendritic nonlinearities, and the precise modulation of the stochastic somatic integration by the oscillatory signal, are not grounded in empirical data. The model also lacks a clear explanation of how the parameters of the diffusion process are mapped onto the neural circuit, making it difficult to evaluate the biological plausibility of the proposed implementation. Furthermore, the current demonstration focuses solely on low-dimensional toy examples, limiting the ability to assess the model's scalability and generalizability to more complex, high-dimensional data.

### Questions
How can the models be tested? What evidence would prove they are correct or falsify them?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes the state-of-the-art diffusive model developed in deep learning could be a running algorithm in recurrent neural circuit. Specifically, it claims the nonlinear dendrites of neurons with globally controlled dendritic noises can be used to implement the reverse phase of diffusive models.

### Strengths
The concept of the present study is original and can significantly advance our understanding of the stochastic recurrent neural circuit once some of my major concerns are solved (see weaknesses). The structure of the manuscript is organized well, and the introduction and discussion are clearly written with a thorough review of the research history as well as possible experimental verification of the theory.

### Weaknesses
I have major concerns about the justification and derivation of two central claims (dendritic nonlinear and global oscillating signal) about neural circuit implementation of diffusive models. A possibility is that the text doesn't explain the key math steps sufficiently well. I look forward to seeing some justification in the rebuttal.

### Dendritic nonlinearity
The paper directly states the nonlinear dendritic operation $f(x_t, \beta_t)$ after Eq. 5 without explaining how it is derived. I am confused about how this nonlinearity comes out. Is it directly from $\mu_\theta (x_{\lambda + t}, \lambda)$ in Eq. 2? In this case, does it imply the dendritic nonlinearity needs to be readjusted if the transition operator in the reverse process is changing? Or it is just used as a way to capture the nonlinearity in biological neurons? Specifically, the paper needs to clarify whether the form of $f(x_t, \beta_t)$ is a direct result of the reverse diffusion process or an assumption made to match the known nonlinearities in real neurons. If it is the former, a clear derivation is needed; if it is the latter, the justification for choosing this specific form should be provided.

### Global oscillating signal
I don't understand how the global oscillating signal is derived. Although the author explained the $\beta_t$ is analogous to the sequence of noise variance in the diffusive model, it seems that the diffusive model doesn't have such an oscillating signal if I understood correctly. I have no idea how Eq. 5 was derived, what assumptions it relies on, and why the $\beta_t$ becomes a sinusoid function there. It is unclear why a sinusoidal function is chosen over other periodic functions or even a non-periodic schedule. The connection between the discrete noise schedule in diffusion models and the continuous sinusoidal oscillation needs further justification. The authors need to explain why a continuous oscillation is necessary or beneficial for the neural implementation, rather than a discrete step-wise change in noise level.

### Training an ANN-based model for dendrites
The author says the dendrite is modeled as an ANN whose parameters were trained via gradient descent. Does this imply some mechanism to adjust the dendritic parameters in real neurons? If so, what are the possible biological mechanisms? I don't see related discussions in the paper. Furthermore, if the dendritic parameters are learned via gradient descent, what is the objective function that is being optimized? Is it directly related to the denoising objective in diffusion models, and if so, how is this objective implemented locally in the dendrites? The paper needs to elaborate on the biological plausibility of learning dendritic parameters through a process analogous to gradient descent.

### Questions
- Fig. 1E caption: why does neural dynamics push off the network off manifold? Does the author mean the neural dynamics of sensory transmission correspond to injecting noise in a similar fashion with the forward process in a diffusive model? At least this neural dynamics is not the same recurrent neural dynamics which the author claims to implement a reverse process to sample from posteriors.

- Fig. 4B caption: it should be (top) and (bottom) because no (left) and (right) here.

- It seems that the iterative steps in diffusive model are indexed by $\lambda$ while that in the neural dynamics was indexed by time $t$. What's the relation between $\lambda$ and $t$? My understanding is that $\lambda$ is a non-negative number while $t$ can go to infinity. Does it imply the equilibrium neural dynamics repeatedly sample distribution of $x_0$ over time?

### Soundness
2 fair

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
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper introduces a novel recurrent circuit model based on diffusion models that incorporates several biologically plausible properties. This method implicitly encodes priors over latent variables and can combine this information with other sources, such as sensory input, to encode task-related posteriors. The approach is mapped to a recurrent network with multi-compartment neuron models, and its effectiveness is demonstrated through experiments on toy datasets.

### Strengths
* The paper successfully maps diffusion model-inspired dynamics to a recurrent circuit with multi-compartment neuron models,

* The modifications to diffusion model dynamics to align with biologically plausible properties are commendable, especially as they do not harm the network quality,

* The provided code is clear and enhances the paper's reproducibility.

### Weaknesses
I think the paper has several weaknesses. Please see the following list and the questions sections.

* Regarding the following sentence in page 5: "First, we tested ... autocorrelation ... remains steadily around zero proving that ... samples are essentially independent." I might agree that the samples are independent. However, isn't it mathematically misleading to use the word "prove" based on correlation? While a zero autocorrelation suggests independence, it does not constitute a formal mathematical proof. A more rigorous approach might involve examining higher-order moments or using statistical tests specifically designed to assess independence.

* Regarding the sentence in page 5: "Overall, these results indicate that the constraints imposed by biology may have a minimal effect on the quality ... compared to DMs". Isn't it too early to state such conclusion. The experiment is on a quite toy-dataset. The current experiments, while promising, are limited to a simplified 2D Gaussian mixture dataset. Generalizing this conclusion to more complex, high-dimensional datasets requires further investigation. It would be beneficial to see results on datasets with more intricate structures and higher dimensionality to assess the impact of these biological constraints on sampling quality in more realistic scenarios.

* The experimental details for the stochastic neural network in Appendix B.2 are lacking, and providing more comprehensive information in this section would strengthen the paper. Specifically, details regarding the network architecture, such as the number of layers, the number of neurons in each layer, and the type of activation functions used, are not clearly specified. Additionally, information about the training procedure, including the optimizer, learning rate, and the number of training epochs, is missing. Providing these details would enhance the reproducibility of the results.

* Overall, the experiments are on quite toy datasets. The reliance on toy datasets limits the ability to assess the scalability and generalizability of the proposed model. While the 2D Gaussian mixture dataset provides a useful starting point, it does not fully represent the complexity of real-world data distributions. Evaluating the model on more challenging datasets, such as MNIST or CIFAR-10, would provide a more comprehensive understanding of its capabilities and limitations.


**Minor Comments**

*  In the second line of Section 2, "nosy" should be corrected to "noisy."

* Figure 1 lacks a caption for (F).

*  In Figure 4 caption (for (B)), it is written "(left) ... (right)" to point out to the corresponding plots, but I guess the caption should use "(top)" and "(bottom)" to indicate the corresponding plots.

* The first line of Section B.3: "Fig. ??" which figure is that?

### Questions
* In Figure 1D, the caption mentions "multi-compartment neuron." Shouldn't it be "multi-compartment neurons"? I thought each gray triangle is a multi-compartment neuron.

* The paper repeatedly mentions "optimized ReLU nonlinearities." I did not really understand the meaning of "optimized" in them?

* Is $\sigma_\lambda$ in Equation 1 the same with $\beta_\lambda$ in Figure 1?

* Regarding the following sentence in page 6: " In principle, this might lead to catastrophic accumulation of errors and large sampling biases; however, the attractor dynamics prevent this from happening." Can authors elaborate on this a bit more? It is not clear to me why?

* In page 6, it is written "$\mathbf{g}\_t (\mathbf{x}\_{t-1}, s) = \frac{1}{\sigma_s^2} \mathbf{M}_s \mathbf{M}\_s^T (\mathbf{x} - \mathbf{x}\_c)$". Is it $\mathbf{g}\_t (\mathbf{x}\_{t-1}, s) = \frac{1}{\sigma\_s^2} \mathbf{M}\_s \mathbf{M}\_s^T (\mathbf{x}\_{t-1} - \mathbf{x}\_c)$?

* Does the last sentence of Figure 3 caption correspond to Figure 3D? There is no caption for (D).

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
