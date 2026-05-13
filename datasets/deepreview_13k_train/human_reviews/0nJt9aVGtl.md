# WaveDiffusion: Exploring Full Waveform Inversion via Joint Diffusion in the Latent Space

- Decision: Reject
- Scores: 6, 3, 6, 3

## Abstract
Full Waveform Inversion (FWI) is a vital technique for reconstructing high-resolution subsurface velocity maps from seismic waveform data, governed by partial differential equations (PDEs) that model wave propagation. Traditional machine learning approaches typically map seismic data to velocity maps by encoding seismic waveforms into latent embeddings and decoding them into velocity maps. In this paper, we introduce a novel framework that reframes FWI as a joint diffusion process in a shared latent space, bridging seismic waveform data and velocity maps. Our approach has two key components: first, we merge the bottlenecks of two separate autoencoders—one for seismic data and one for velocity maps—into a unified latent space using vector quantization to establish a shared codebook. Second, we train a diffusion model in this latent space, enabling the simultaneous generation of seismic and velocity map pairs by sampling and denoising the latent representations, followed by decoding each modality with its respective decoder. Remarkably, our jointly generated seismic-velocity pairs approximately satisfy the governing PDE without any additional constraint, offering a new geometric interpretation of FWI. The diffusion process learns to score the latent space according to its deviation from the PDE, with higher scores representing smaller deviations from the true solutions. By following this diffusion process, the model traces a path from random initialization to a valid solution of the governing PDE. Our experiments on the OpenFWI dataset demonstrate that the generated seismic and velocity map pairs not only exhibit high fidelity and diversity but also adhere to the physical constraints imposed by the governing PDE.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The manuscript introduces a new approach to invert acoustic wave equation data based on a joint generative process. Although there were earlier papers on the use of generative models for data inversion, the presented approach looks fairly original. The authors study the famous geophysical problem known as full waveform inversion (FWI). The approach was tested on 2D spatial data from public dataset OpenFWI.

### Strengths
Generative AI is transforming different industries in our days and its use for data inversion looks like a promising research direction. Both theoretical and experimental parts are well-present and easy-to-follow. An important original feature of the work is joint generation of acoustic data and velocity models.

### Weaknesses
1.	It is not clear (at least none of the experiments show this) how to use the presented algorithm to invert actual data. It is shown how to generate acoustic data and velocities. But what is typically expected by the reader is the answer on what to do when we are given with some specific seismic data.
2.	Section 4.2.3 Comparison with Inversionnet is not sufficiently complete and convincing. See Questions below.
3.	The geophysical terminology is mixed in the manuscript. Notice the used wave equation models $acoustic$ data. This is a significant simplification of seismic phenomena. In other words, the terms $acoustic$ and $seismic$ are not interchangeable.

### Questions
1.	How acoustic data and velocity models were preprocessed before training?
2.	The authors trained the model for 1000 epochs. How long was it in terms CPU/GPU time (depending on the dataset)?
3.	The discussion in the manuscript covers only generation and inversion of 2D spatial data. While 3D models/data are of much higher interest.  Could the proposed algorithm be used in the 3D case? What will the implication on computational complexity?
4.	An important test for an inversion code is to check that symmetric data with respect to some plane produces a symmetric velocity model. Would the presented generation model obey this principle?
5.	It is not clear from the experiments how the presented algorithm compares to baselines. Section 4.2.3 Comparison with Inversionnet does not give the answer on the obvious question: which of the two algorithms is better.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The paper introduces a new framework for Full Waveform Inversion (FWI) that uses a joint diffusion process in a shared latent space. This approach merges the bottlenecks of two separate autoencoders (one for seismic data and one for velocity maps) into a unified latent space.

### Strengths
The paper is well written and the diffusion approach in the latent space is an interesting extention to dual autoencoder approaches. With convincing results to support this research.

### Weaknesses
My major problem with this manuscript is that the main approach to generating two joint autoencoders is not novel. A similar approach including similar experiments has been proposed and published the approach on dual autoencoder before this submission (https://arxiv.org/pdf/2305.13314) and another publication on dual autoencoder can be found at (https://arxiv.org/pdf/2405.13220). These contributions are neither acknowledged nor cited.  The remaining novelty is the diffusion process within the latent spaces which is by itself an interesting idea and should have been stated as the contribution of this manuscript.

### Questions
Please address the weaknesses.

### Soundness
3

### Presentation
3

### Contribution
1

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
Full waveform inversion (FWI) is a seismic imaging technique that traditionally reconstructs the subsurface velocity model by iteratively comparing observed and predicted seismic data. More recently, machine learning-based approaches would solve FWI by treating it as an image-to-image translation problem. Furthermore, generative diffusion models mainly treated FWI as a conditional generation problem where the velocity map is generated from a given seismic data. This paper offers a new perspective on FWI by considering it as a joint generative process. Namely, the paper considers whether the two modalities -- seismic data and velocity map -- can be generated simultaneously. Two key steps are proposed: first, a dual autoencoder encodes the two modalities in a shared latent space that provides a coarse approximation of the wave equation solution. Second, a diffusion process in the latent space refines the coarse latent representations which are later decoded into seismic data and velocity maps. In contrast to seismic-velocity pairs generated by the conditional models which often lack physical consistency, the jointly generated pairs approximately satisfy the governing PDE without any additional constraint. The paper's main goal is to offer a new perspective by extending FWI from a conditional generation problem to a joint generation problem.

### Strengths
- The proposed paper is well-organized and the idea is clearly presented.
- The paper offers a new perspective on the FWI generation problem by simultaneously generating two modalities -- seismic data and velocity maps -- from the shared latent space. This is a novel idea in contrast to the existing related work which treats these two modalities separately.
- Treating seismic data and velocity maps separately limits the ability to generate physically consistent seismic-velocity pairs. In contrast, jointly generating these modalities makes them approximately consistent with the governing PDE that describes the relationship between them.
- The extensive experiments confirm the soundness of the proposed method and show that the jointly generated seismic-velocity pairs can be a useful supplement to real training data.

### Weaknesses
I think there are three main problems in the experiments:
- The method wasn't compared to any existing conditional generative methods. There is even a section 4.2.4. that compares separate vs. joint diffusion but there the separate diffusion was the same model as for the joint diffusion but with a single branch kept active and the latent space no longer shared. I think it would be useful to see how the proposed method compares to the existing methods (e.g., [1]) both in terms of the diversity of the generated data and the performance of the reconstruction methods when trained on the generated data.
- The results might also differ based on a different reconstruction method other than InversionNet (e.g., [2] and/or [3]). I think it would be beneficial to add at least one additional data-driven solver.
- Some of the experiments in the results section do not seem to be realistic. (see more in the questions section)

### Questions
1. Could you comment on the comparison with the existing conditional generative models? Why didn't you compare to any of the existing methods at least in 4.2.4 section?
2. Could you comment on the choice of the reconstruction method? I think it would be beneficial to add at least one additional data-driven solver. It would be interesting to see how the reconstruction methods work with data generated by different generative models.
3. The generative model was trained on the same OpenFWI dataset on which InversionNet was later evaluated. What is the amount of data your generative model should be trained with and how does it compare to the size of a dataset reconstruction methods (e.g., InversionNet) should be trained with? If the size of a dataset for reconstruction methods is satisfying what is the rationale of doing this? I think you should address the limitations of such a setup.
4. In continuation to the previous question, how realistic is the Gen+1\% case? In this case, you trained your generative model on the same data distribution as in the 1\% of the original dataset. If a real dataset is small, wouldn't it be more realistic to train your generative model with real data that differ from the distribution in the small dataset? Maybe a more realistic case would be to train the generative model on the two subsets and add 1\% of the third subset of OpenFWI. Could you comment on this? What are the implications of the existing setup for real-world applications of the method?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper deals with the problem of full waveform inversion.
There are two mechanisms that the paper proposes.
1. The paper uses the same latent space for both the model and the data
2. They train a diffusion model in the latent space. Such a diffusion model can therefore generate a plethora of models and their data.

Results look reasonable even though the models that are being trained on are very simple.

### Strengths
The idea of using a joint feature space is good and then using a diffusion model on this space is also a good idea. The results are interesting and it seems that the approach works for the models in the data base.

### Weaknesses
Unfortunately, the idea of using an AE with common feature spaces for data and model is not new. See https://paperswithcode.com/paper/paired-autoencoders-for-inverse-problems
This is the main problem that the paper have. I understand that in this fast moving field some papers are missed but in this case, the work that was already done makes much of the paper not relevant.
I would recommend the authors to withdraw the paper, concentrate of the diffusion aspect of the paper and resubmit to a different venue.

### Questions
The interesting parts of the paper are actually hiding towards the end.

1. How do you actually do coarse to fine?

2. Given some data $d$ how to you use diffusion to find an appropriate model

I would recommend re-writing the paper with section 3.3 in mind. Since training a dual AE is not very innovative and using diffusion of the latent space is not very innovating, the innovation is exactly what you do in 3.3. You could easily develop it to a full paper.

### Soundness
3

### Presentation
2

### Contribution
2
