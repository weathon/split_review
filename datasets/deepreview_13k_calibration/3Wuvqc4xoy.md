# Learning Efficient Representations of Neutrino Telescope Events

- Decision: Reject
- Avg Score: 3.75
- Scores: 3, 8, 3, 1

## Abstract
Neutrino telescopes detect rare interactions of particles produced in some of the most extreme environments in the Universe.
This is accomplished by instrumenting a cubic-kilometer volume of naturally occurring transparent medium with light sensors. 
Given their substantial size and the high frequency of background interactions, these telescopes amass an enormous quantity of large variance, high-dimensional data.
These attributes create substantial challenges for analyzing and reconstructing interactions, particularly when utilizing machine learning (ML) techniques.
In this paper, we present a novel approach, called \texttt{om2vec}, that employs transformer-based variational autoencoders to efficiently represent neutrino telescope events by learning compact and descriptive latent representations.
We demonstrate that these latent representations offer enhanced flexibility and improved computational efficiency, thereby facilitating downstream tasks in data analysis.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This article presents an approach to learning representations of neutrino events by leveraging a transformer-based variational autoencoder. The model is trained to capture the photon arrival time distribution, and the learned representations are evaluated using the Jensen-Shannon divergence to assess reconstruction quality. Furthermore, the authors explore the applicability of these representations in a downstream task – angular reconstruction.

### Strengths
The application of machine learning techniques in scientific research is a vital and rapidly evolving field. We are delighted to see submissions in this area and encourage researchers to share their relevant work.

### Weaknesses
This article requires significant improvements in its writing and technical accuracy. Numerous technical details are either unclear, incorrect, or require further clarification (see Questions for specific concerns). As it stands, the article's technical clarity is compromised, which may lead to confusion and misinterpretation. A thorough revision is necessary to ensure the article's technical details are accurate, clear, and concise.

* In Fig. 2, the “autoencoder” outputs some probabilities through the softmax activation. This is a confusing design. How is the reconstruction loss applied in this case?
* In section 4.2, the training methodology for the three models and the utilization of om2vec are unclear. Can you provide a more detailed explanation of the training process and how om2vec is incorporated?
* Are there any additional physics features that could be included in the time series data, beyond the current single feature of photon hits?
* In lines 179-180, the authors wrote “We opted for a learnable memory embedding for the transformer decoder layers, ensuring that the decoder portion of the architecture remains entirely independent of the encoder”. Please elaborate on the memory embedding block about its design.
* The model and training details in Table 1 are incomplete and unclear. Can you provide a more comprehensive description of the model architecture, including the number of encoder and decoder layers used?

### Questions
* In Fig. 2, the “autoencoder” outputs some probabilities through the softmax activation. This is a confusing design. How is the reconstruction loss applied in this case? 
* In section 4.2, the training methodology for the three models and the utilization of om2vec are unclear. Can you provide a more detailed explanation of the training process and how om2vec is incorporated?
* Are there any additional physics features that could be included in the time series data, beyond the current single feature of photon hits?
* In lines 179-180, the authors wrote “We opted for a learnable memory embedding for the transformer decoder layers, ensuring that the decoder portion of the architecture remains entirely independent of the encoder”. Please elaborate on the memory embedding block about its design.
* The model and training details in Table 1 are incomplete and unclear. Can you provide a more comprehensive description of the model architecture, including the number of encoder and decoder layers used?

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper presents om2vec, a novel approach leveraging transformer-based variational autoencoders (VAEs) to create compact, descriptive latent representations of photon arrival time distributions (PATDs) from neutrino telescope events. The proposed model is designed to handle the high-dimensional, variable-length data typical of neutrino observatories like IceCube. om2vec aims to outperform conventional approaches, such as asymmetric Gaussian mixture models (AGMMs), by improving reconstruction accuracy, runtime efficiency, and reliability while being less dependent on hyperparameters. The paper details the architecture, training, and testing with simulated datasets, comparing the method’s performance with traditional AGMMs and exploring its utility for downstream tasks like angular reconstruction.

### Strengths
- Originality: Applying transformer-based VAEs to neutrino event data is novel and demonstrates a creative extension of ML techniques to physical sciences.
- Quality: Comprehensive evaluation of the model against AGMMs, showing significant improvements in reconstruction accuracy, computational efficiency, and robustness.
- Clarity: The architectural details, data processing steps, and experimental methods are described with clarity, making the paper accessible to readers familiar with ML and neutrino physics.
- Significance: The ability to improve data processing and enable better downstream analyses has substantial implications for neutrino research and potentially for other high-dimensional physics datasets.

### Weaknesses
 - Generalizability: While the results are promising, it would be helpful to see a more extensive discussion on how the method might generalize across different types of neutrino observatories or non-simulated real-world data.
- Comparison Baseline: Although om2vec is compared with AGMMs, additional comparisons with other potential ML approaches (e.g., deep CNNs or LSTMs) for PATD representation might strengthen the case for its use. Specifically, the lack of comparison with methods that directly operate on the raw time-series data, rather than extracted features, is a notable gap. This is important since the transformer architecture is well-suited for time-series data.
- Hyperparameter Sensitivity: While the model claims reduced dependence on hyperparameters, an exploration of performance variability with different encoder/decoder block configurations or latent dimension sizes would provide deeper insights into its stability. The paper should include a sensitivity analysis showing how performance metrics vary with these key architectural choices, including the number of attention heads and the dimensionality of the hidden layers within the transformer blocks.

### Questions
1. How does the model’s performance vary with different encoder/decoder block architectures or deeper networks?
2. Can the approach be adapted or extended to handle data from other types of particle physics experiments with different signal characteristics?
3. Have real-world data tests been considered, and if so, what were the challenges and results?
4. Is there potential for this method to contribute to real-time data processing in neutrino observatories under field conditions?

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This develops a variational autoencoder to create a generative model for data produced by neutrino telescopes. The architecture is based on transformers, and results in a flexible representation and improved computation.

### Strengths
The application is certainly interesting and compelling. I also like the rationale of the work. There's a clear scientific motivation for these problems.

### Weaknesses
Several aspects. First, this is an ML focused conference so I would have appreciated greater details on the encoder and decoder without having to dig through the source code. Why transformers as opposed to a simpler architecture? Is there some kind transformation of the features that would allow for an MLP. Even if not, I would appreciate these as baselines as opposed to a traditional statistical model when comparing performance.

Also having worked with these a lot, I'm willing to bet that there was a substantial amount of tweaking required for learning rate and architecture parameters. If not, I'm certain performance can be improved dramatically by taking these steps. Another example, the runtime isn't really compelling to me. This is a feed-forward network, clearly it's going to be quicker than the alternatives. Should be supplementary, which would make more space for the fitting details I discussed.

Overall, this seems written for a scientific audience rather than an ML audience. I very much appreciate the application and clear motivation so I hope it's resubmitted. It just seems like some of the details we find interesting were glossed over and need to be improved for this to be accepted.

### Questions
Not at the moment, will see other reviewers' comments.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
1

### Rating Number
1

### Confidence
4

### Summary
The paper titled "Learning Efficient Representations of Neutrino Telescope Events" introduces a novel approach called om2vec, which utilizes transformer-based variational autoencoders (VAEs) to effectively represent neutrino telescope events. The study addresses the challenges posed by high-dimensional, variable-length Photon arrival time distributions (PATDs) recorded by optical modules in neutrino telescopes, particularly focusing on the IceCube Neutrino Observatory.

### Strengths
- The use of a transformer-based variational autoencoder (VAE), called om2vec, represents an innovative approach for neutrino event data analysis, which has traditionally relied on more conventional statistical methods or simple summary statistics. 
- The paper pushes the boundaries of machine learning applications within high-energy physics, specifically neutrino detection. 
- By applying a VAE with transformer components to a unique scientific data source, the paper contributes to bridging techniques between disciplines, such as physics, machine learning, and data science. This could encourage further cross-disciplinary research and adaptation of machine learning models to complex scientific problems.

### Weaknesses
 - The paper lacks a clear structure and does not adequately address related work. If this is indeed the first study applying deep learning techniques to the domain of neutrino telescopes, it is essential to include a dedicated **Related Works** section to provide context for this research.

- The figures in the paper are oversized. I recommend the authors resize them to a more standard dimension to enhance the overall presentation quality. The current size does not meet the standards expected for conference presentations.

- There are several typographical errors throughout the paper (e.g., lines 127, 484, etc.), which detract from its readability and should be addressed to improve clarity.

- The objective function is unclear, and the problem is not well-defined. The paper jumps directly to the results, with only a brief discussion of the classical $KL$ divergence. A significant improvement is needed in presenting a comprehensive **Proposed Methods** section that clearly defines the final objective function, rather than merely referring to it in the **Results section** (lines 228 to 230).

- Some statements in the paper are ambiguous or inaccurate. For example, the assertion in lines 223 to 232 that "the re-parameterization trick is utilized to construct the latent representation $z$, a vector of user-defined length referred to as the latent dimension. This technique guarantees that the latent space remains continuous and that similar representations within this space reconstruct to similar PATDs" is misleading and not entirely accurate.  However, the reparameterization trick separates the randomness of sampling (handled by $\epsilon$) from the parameters $\mu$ and $\sigma$, which allows to compute gradients with respect to these parameters. I recommend that the authors deepen their understanding of this concept from this paper [1].

### Questions
The paper is somewhat limited as it presents results solely based on training and testing with simulated events, which may not accurately reflect real-world measurement data. Given that the approach uses a VAE-based transformer, it may perform better with simulated data that follows known distributions. Do you have access to any existing real-world datasets? If so, I would appreciate your feedback on this aspect.

### Soundness
2

### Presentation
1

### Contribution
1
