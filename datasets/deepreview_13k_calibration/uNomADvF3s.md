# Lift Your Molecules: Molecular Graph Generation in Latent Euclidean Space

- Decision: Accept
- Avg Score: 6.50
- Scores: 6, 8, 6, 6

## Abstract
We introduce a new framework for molecular graph generation with 3D molecular generative models. Our Synthetic Coordinate Embedding (\ours{}) framework maps molecular graphs to Euclidean point clouds via synthetic conformer coordinates and learns the inverse map using an E($n$)-Equivariant Graph Neural Network (EGNN). The induced point cloud-structured latent space is well-suited to apply existing 3D molecular generative models. This approach simplifies the graph generation problem -- without relying on molecular fragments nor autoregressive decoding -- into a point cloud generation problem followed by node and edge classification tasks. Further, we propose a novel similarity-constrained optimization scheme for 3D diffusion models based on inpainting and guidance. As a concrete implementation of our framework, we develop \ourswithedm{} based on the E(3) Equivariant Diffusion Model (EDM). \ourswithedm{} achieves state-of-the-art performance in distribution learning of molecular graphs, outperforming the best non-autoregressive methods by more than 30\% on ZINC250K and 16\% on the large-scale GuacaMol dataset while improving conditional generation by up to 3.9 times.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The paper introduces a novel 3D latent embedding scheme for 2D molecular graph generation. It presents a set of experiments which try to show that this inductive bias is helpful for a set of 2D molecule generation tasks.

### Strengths
The model and experiments are clearly described. The paper acknowledges the importance of generation tasks beyond vanilla distribution matching on the space of 2D molecular graphs. The experiments are chosen to attempt to shine light on the effectiveness of the 3D latent inductive bias hypothesis.

For guided generation, the comparable results with "Translation" methods are impressive.

### Weaknesses
The experiments are ambiguous on whether this inductive bias is, indeed, helpful.

It appears from table 3 that results on the ZINC250K dataset are saturated. The FCD and KL values reported in Table 4 are interesting, but presented without much interpretation. Without prior expertise it is difficult to evaluate FCD scores. Furthermore, de novo generation is not a terribly useful task in practice.

The most compelling experiment presented in the paper is "Similarity-Constrained Optimization". I could see how a 3D latent would improve performance in this area, but the data presented for this section is scant.

Overall, none of the experiments prove or disprove the inductive bias hypothesis of the architecture.

### Questions
What is the KL divergence references at the end of page 8? The description "a variety of physiochemical descriptors" is too vague. Sorry if I missed a more precise definition elsewhere.
Is there a reason the results for "Similarity-Constrained Optimization" are not presented in more detail in the main paper? This is by far the most real-world useful application, and the one which has the highest probability of showing signal on your hypothesis (in my opinion).

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
3

### Summary
This paper proposes a new method for 2D molecular graph generation using 3D molecular diffusion models, using the following steps:
- Train an autoencoder on paired (2D molecular graph, latent 3D molecular graphs).
  - The encoder consists of two parts:
       - First, 3D coordinates for all atoms are obtained using ETKDG, an well-known 3D conformation generation algorithm. No learning is required here.
       - Then, an EGNN is used to map the 3D molecular graph to a latent 3D graph, with updated node features and coordinates. The idea here is to incorporate neighborhood information for easier decoding of atom and bond types (as seen in Appendix G.1).
   - The decoder consists of two MLPs: one to predict atom types, and another to predict the bonding between the atoms.
The encoder and decoder are trained in the standard variational (VAE) framework.
* Train a diffusion model to generate latent 3D molecular graphs.
Here, the authors use the well-known EDM model (Hoogeboom, et al. 2022).
While the task is similar to that of standard 3D molecular graph generation, here the latent 3D molecular graphs do not necessarily correspond to anything physical)
* To sample:
    - Run the diffusion model, starting from noise, to generate latent 3D molecular graphs.
    - Run the decoder on the latent 3D molecular graphs to get 2D molecular graphs.

First, the authors compare their framework (EDM-SyCO) to GeoLDM, a 3D molecular graph generation algorithm combined with a simple bond prediction algorithm to create 2D molecular graphs. They show that the performance drops significantly. However, it is unclear whether the performance drop is due to the inaccurate bond prediction, or the use of standard 3D molecular graphs instead of the author’s latent 3D molecular graphs.

Next, the authors compare their model to autoregressive baselines on the well-established ZINC250K and GuacaMol datasets. They find that their model outperforms existing all-at-once 2D graph generative models. However, the performance improvement over state-of-the art autoregressive models is unclear, especially on the larger GuacaMol dataset.

Overall though, this is an interesting idea for 2D molecular graph generation. My only real concern is that the utility of the EGNN latent space is not conclusively shown; I have mentioned two experiments in the first bullet point of my Weaknesses section that I would love to see performed.

EDIT: I am happy with the author's response and additional experiments, and have increased my score in response.

### Strengths
- The paper is very well-written and full of details which are hard to find in most papers on this topic.
- The overall idea is definitely interesting and novel; it matches up with geometric intuition that molecules naturally live in 3D space.
- The authors have definitely improved results for non-autoregressive models on ZINC250K.
- Experiments on inpainting and conditional generation are creative, and quite comprehensive.

### Weaknesses
 - If the motivation for having an EGNN in the encoder is to incorporate neighborhood information for predicting atom and bond types for decoding, I would have liked a comparison to a setup where the EGNN is used as a decoder (over the simple MLPs). To summarize this scheme:
    - The encoder would just output the ETKDG-generated coordinates.
    - The decoder would be an EGNN + MLP to predict atom and bond types.
    - A diffusion model could then generate (as standard) 3D molecular graphs. In fact, any pretrained diffusion model could be used, in contrast to the author’s scheme here where the diffusion model must target the latent space of the EGNN encoder.

 - In Section 6.1, I would have liked to see GeoLDM paired with a more sophisticated bond-determining algorithm such as RDKit's rdDetermineBonds (an implementation of xyz2mol) or OpenBabel. For example, as shown in Table 1 of https://openreview.net/pdf?id=MIEnYtlGyv, there can be significant variation in the results from each of these bond-determining algorithms. This could help prove the utility of the EGNN latent space for the diffusion model to target.

I would be willing to increase my score if the above experiments are performed convincingly.

 - Training time seems high (~10 days on a single A100 GPU) relative to other methods; this is probably related to why the authors did not tune hyperparameters on the GuacaMol dataset. I would like a confirmation from the authors on this point.

### Questions
- How does your model handle chirality, since the diffusion model is E(3)-equivariant? This could motivate the use of SE(3)-equivariant GNNs instead.
- Section 6.2: Please report how the normalization of the FCD and KL divergence metrics was performed for clarity.
- How is the novelty metric so high? This is very different from the 3D molecular graph generation setting (Appendix C of https://arxiv.org/abs/2203.17003) where the novelty usually reduces as training progresses. (This might be because the datasets for 3D molecular generation such as QM9 are the exact enumeration of all compounds with a certain property. However, it is surprising to see a novelty score of 100% in any case, indicating that none of the training molecules were sampled.)
- Some experiments on generalization would be very nice to see; can you train only on smaller graphs but generate much larger ones?
- Line 503 has a typo: “... factors 2.7 ad 15.6”
- Analysis of invalid molecules would be good, especially to motivate future work.
- Comparison of training and sampling time to other models would be nice, to understand the tradeoff between compute and performance better.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This work presents a 2D molecule graph generation method that uses 3D molecule generative models by mapping 2D molecule graphs to 3D point clouds via synthetic coordinates and learning the inverse mapping using EGNN. Based on EDM, the proposed method shows superior generation quality.

### Strengths
- As molecules have 3D structures, using the 3D information to generate 2D molecular graphs seems intuitive and reasonable.

- The reconstruction accuracy ablation study on autoencoder shows the justification of using EGNN architecture.

- The framework can also be used for conditional generation/optimization of molecules in diverse settings, such as scaffold-constrained generation and similarity-constrained optimization.

- The experimental results show the effectiveness of this approach.

### Weaknesses
Although using latent Euclidean point clouds instead of a simple 2D graph structure seems to be a reasonable and effective way of modeling molecular graphs, it is likely that this approach is not scalable with respect to the molecule size. Working with latent point clouds would likely require far higher computational costs and memory compared to previous diffusion models. Especially, it seems that learning the 3D information of large molecule structures would be challenging compared to learning the 2D graph distribution. Is there any experiments or explanations on this issue?

### Questions
Please address the weakness mentioned above.

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
4

### Summary
**Summary:** The authors present SyCO as a straightforward method for generating 2D graphs using 3D generative models.

**Recommendation:** Given the notable strides yet remaining work to be clarified, discussed, or explored in this manuscript, I am currently recommending a weak reject.

**Rationale behind Recommendation:** If the authors can discuss some of the empirical benchmarking shortcomings of their model (e.g., what future steps might look like) and also include a small sample of experiments using a geometric neural network architecture other than EGNNs (to verify that the authors' ideas generalize beyond this architecture), I will consider raising my score.

### Strengths
- SyCO's simplicity and versatility should encourage more development in the intersection of 2D and 3D graph generation models.
- SyCO's autoencoding reconstruction performance for bond type prediction is compelling.
- The authors provide a succinct and well-motivated case study of how to add atoms to a molecule during molecular optimization via diffusion generation.
- The authors' classifier guidance is well explained and motivated for property-specific molecule generation and optimization.
- The authors' code is well documented.

### Weaknesses
 - SyCO borrows most of its diffusion methodology from previous works [1, 2], to the best of my knowledge with adding nodes during inpainting being the only notable example to the contrary.
- Although it is simple to start with, the EDM architecture is no longer state-of-the-art for 3D molecule generation [3], suggesting the authors' results could be improved with a different choice of e.g., geometric GNN architecture. The authors seem to have a taken a wide approach to benchmarking rather than a deeper approach to seeing which geometric GNNs can best encode 2D graphs as latent 3D point clouds. This latter area of investigation could strengthen this work notably.
- The authors' conditional generation results for LogP in Table 5 and diversity throughout Table 6 seem a bit underwhelming. Besides attributing this as a flaw of molecule denoising networks, it would be helpful for the authors to expound how they think these results might be improved over time.
- The authors should discuss the pros and cons of relying on RDKit for conformer generation. For example, are there inherent biases in its distance-based coordinates estimation algorithm that might limit or impact the behavior of molecule generative models trained on its coordinate embeddings?

### Questions
- The authors should clarify what the error bars in Table 3 represent. Standard deviations across 3 runs of a model, as in Table 4?

### Soundness
3

### Presentation
3

### Contribution
2
