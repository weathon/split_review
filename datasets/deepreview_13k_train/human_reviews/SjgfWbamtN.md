# MiniFold: Simple, Fast and Accurate Protein Structure Prediction

- Decision: Reject
- Scores: 3, 6, 5, 3

## Abstract
Protein structure prediction has emerged as a powerful tool for biologists and drug makers. However, the computational toll associated with state-of-the-art models, such as AlphaFold2 or ESMFold, hinders their use in large-scale applications like virtual screening or mutational scanning, where a single experiment may involve processing millions of protein sequences. In an effort to develop a more efficient model, we aimed to understand which of the complex architectural choices proposed in AlphaFold2 were essential to achieve high performance, and which could be omitted without significantly compromising accuracy. This analysis culminated in a simple, yet highly expressive architecture for protein structure prediction. Our model, MiniFold, consists of a minimal Evoformer variant, a parameter-free coordinate recovery algorithm, and a custom hardware-optimized implementation composed of newly designed GPU kernels. When compared against ESMFold, MiniFold achieves over 100x speedup and shows improved scalability to long protein sequences while conserving over 95% of the original performance, making it a promising candidate for large-scale applications.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper presents MiniFold, a highly optimized protein structure prediction model that achieves over 100x speedup compared to ESMFold while retaining 95% of its accuracy. MiniFold simplifies the Evoformer architecture by removing unnecessary components like sequence encoding, triangular attention, and recycling. It also implements efficient GPU kernels and a simple coordinate recovery module.

### Strengths
- The analysis to identify key components of Evoformer that enable high performance protein folding is insightful. This allows simplifying the architecture while maintaining accuracy.
- The 100x speedup over ESMFold enables the application of protein folding models to high-throughput tasks involving millions of sequences. This is a major contribution.

### Weaknesses
 - The prediction process is faster, but final performance significantly decreases.
- Removing IPA is disadvantageous, as the structure module is less costly than Evoformer.
- Kernels are implemented with OpenAI's Triton, not CUDA; a full-page explanation is unnecessary due to well-known engineering improvements.
- The analysis of kernels is wrong. For example, "This reduces the number of reads from 5 to 1, and the number of writes from 4 to 1". The Wx and Vx are matrix multiplication operators, which will call GEMM kernels, thus these read/write cannot be merged. We usually can only save the read/write times for element-wise operators.
- The method relies on a computationally demanding pretrained protein language model; simplification would be beneficial.
- Coordinate recovery omits chirality consideration, potentially negatively impacting performance.
- In-depth analysis of uncertainty estimation technique is needed for better understanding of robustness.

### Questions
- I notice there are confidence scores, but where you do inject randomness to generate a distribution?
- Could training with MSAs further improve MiniFold's accuracy? What optimizations would be needed?
- In Sec 4.2, how do you perform MiniFormer with recycling based on MDS?
- Do you end-to-end optimze the coordinates with gradient back-propagation, or just the Distogram?
- Do you include the time cost of ESM when compute time cost in Sec 4.2?
- Does the comparison in Sec 4.2 include the gradient backward time?
- Are there standalone efficiency comparsion (compared with the ones without kernels) for the two optimized kerenls?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper tackles the protein folding problem, an important and time-consuming task. The authors proposed MiniFold that can infer a structure with 100x acceleration and tolerable accuracy loss. To achieve this, they carefully studied each block in EvoFormer, removed unnecessary blocks, and proposed a new pipeline. Experimental results demonstrate the effectiveness of their algorithm.

### Strengths
Overall, I pretty much enjoy reading this paper. The motivation and intuition are clear, and the way the authors solve the problems is reasonable. In addition, the contribution is indeed significant, especially under large-scale screening demand. The paper is well-written and organized, and the demonstration is straightforward.

### Weaknesses
Currently, I give a score of 6. I am happy to increase my score if the below weaknesses (and questions) can be appropriately addressed.

-  First of all, the authors clearly have dived into the (time and performance) ablation of AlphaFold2, ESMFold and MiniFold, which will be great to present. For example, how do time and performance change if we remove the triangular attention blocks? How is the performance change if we recycle MiniFold once / twice / third times?Theses results are not only useful for the design of MiniFold, but are also knowledge that people are curious about.
- The second question relates to the third part of MiniFold (structural determination based on distance matrix). Why can't you directly build the 3D $C_\alpha$ backbone based on the distance matrix (assuming that the matrix is filled)? In addition, how do you determine the side-chain angle?  
- Third, I noticed that you built the model on a smaller (but pre-trained) ESMFold, right? In fact, one of the reasons why ESM and AF2 are so huge is that they train *from scratch*. I am not saying that using previous embeddings is not good, but an intermediate path to address the efficiency problems is to distill or prune the ESM model, or to use it as a teacher model to train a smaller model (since you have an infinitely large dataset now). Do you know any work about how this would be compared to MiniFold? What do you think is the pros and cons of different solution paths?
- A minor point, I don't think "removing" cycling can be counted as your acceleration. This is entirely a time/accuracy trade-off, and can be easily achieved. I'd suggested the authors cycle MiniFold as well and compare the time.
- Last but I am indeed curious: you mention that the Multiplicative layer can replace attention. Can you show how the performance changes after the replacement? In addition, this is also applicable to other fields, so I am curious why do you think this replacement can work well, and is it a domain-specific thing or not?

### Questions
I have asked many questions above.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes an efficient protein structure prediction method. The authors use ESM-2 to extract residue features and construct pairwise representations. The pairwise features are used to predict pairwise distance between all residues. Finally, they recover  3D coordinates from
the predicted distogram based on multi-dimensional scaling.

### Strengths
1. The paper is clearly written.
2. The main strength of MiniFold is good efficiency. The proposed MiniFold achieves over 100x speedup.
3. The authors simplified the modeling complexity and did GPU kernel optimization.

### Weaknesses
1. The proposed methods only generate C-alpha atoms. It could not reconstruct full-atoms.
2. Most of the neural modules were copied directly from existing literature, limiting the novelty.
3. The authors do not provide code for checking.

### Questions
1. Could the author provide TMScore comparisons against AlphaFold, Omegafold, and ESMFold on long proteins (protein size>1000)? 

2. Have you tried to reconstruct full-atoms? 

3. Considering the importance of the structural prediction task, it should be carefully examined. Could the authors provide the source code?

4. Does the inference time cost take into account the overhead of the coordinate realization module?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
AlphaFold2 remains the state of the art for protein structure prediction. However, the model has poor complexity characteristics and high peak memory usage, and inference on longer proteins often runs for several minutes or more. The authors propose MiniFold, a barebones, single-sequence architecture built with select modules from AlphaFold2. Despite the model's small parameter count, it achieves a high fraction of ESMFold's single-sequence performance on CAMEO proteins and runs faster.

### Strengths
The paper is clearly written and easy to follow. Some of the ablations are fairly surprising (e.g. recycling) and, if supported by better evaluations (see below), would improve our understanding of the all-important AlphaFold2 architecture. The proposed model is fast and fairly performant, and could make a useful addition to the structure prediction toolbox.

### Weaknesses
- Since MiniFold only predicts the backbone structure, the comparison to architectures like AlphaFold2 and ESMFold is a little bit unfair. It's unclear from this manuscript whether ablated components are actually unnecessary or necessary to predict the positions of atoms excluded here.
- There are a lot of important baselines missing here. RGN2 (Chowdhury et al., 2021) is a lightweight structure predictor with a language model that purports to be faster than AlphaFold2 by six orders of magnitude. Optimized versions of the full AlphaFold2 like FastFold (Cheng et al., 2022), UniFold (Li et al., 2022), and recent versions of OpenFold (Ahdritz et al., 2022) also exist but are not tested here. RosettaFold2 is also missing.
- CAMEO evaluation is not sufficient to tease out the differences between structure prediction models. The gold standard is CASP proteins, which often reveal much larger gaps between models than can be seen in CAMEO figures alone. ESMFold famously underperformed AlphaFold2 at CASP15 by a very wide margin, and I suspect the limited capacity of MiniFold could hold it back even further here.
- Originality isn't the only criterion here, but I'm not sure if this paper has many new insights that would be of interest to the broader machine learning community. The observation that triangle attention isn't strictly necessary was already noted in the original AlphaFold2 paper. Other more surprising claims (recycling isn't necessary) need to be supported by additional evidence, like a CASP evaluation. As I mentioned above, this isn't the first paper to present an optimized, protein-language-model based lightweight alternative to AlphaFold2 either.

Bits and bobs:

> Our analysis reveals that the bulk of the compute is spent in the Evoformer blocks, which is responsible for predicting the pairwise interactions between the protein residues. Specifically, the Triangular attention layers of the Evoformer have O(n3) time and memory complexity, which hinders scaling to longer sequences.

- This is a bit grandiose. The complexities of the AlphaFold2 modules are already well-known.

> The main limitation of AlphaFold2, however, is its computational cost

- I wouldn't call this the "main" limitation. The model isn't that great at proteins without deep MSAs, e.g..

>We constructed a training set from the AlphaFold database. In particular, we first cluster the sequences from Uniref50 (Suzek et al., 2007) at 30% sequence similarity, and then select the structures with an average plDDT score above 0.7. This results in a high quality, diverse dataset of roughly 10 million structures.

- If you're training on AF2 structures, especially exclusively, then a lot of your claims about certain components of AF2 being unnecessary could be called into question; this is effectively a form of distillation, not an independent competing architecture.

>Our results show that MiniFold is competitive with other protein language model based structure prediction models, achieving over 95% of the state-of-the-art ESMFold at a fraction of the computational cost.

- 95% is somewhat misleading. OpenFold shows that the full AlphaFold2 model reaches comparable lDDT levels almost immediately; almost all of the training time is spent closing roughly the same gap as the one between MiniFold and the full AlphaFold2 model.

### Questions
>We perform several modifications to the Evoformer architecture, as shown in figure 2. First, we eliminate the sequence-level encoding and keep only the pairwise representation and update. Remarkably, this reduces the number of parameters from over 600 million to merely 3 million. In fact, we argue that the representational capacity of the Evoformer is influenced by the depth and complexity of its operations rather than by its parameter count.

- Where does 600 million come from? AlphaFold2 has about 93 million parameters.

>In addition, we eliminate the recycling operation used in both AlphaFold2 and ESMFold, as we found it only provides very minimal benefits that did not outweigh the additional computational cost.

- This contradicts the ablations in the AlphaFold2 paper. In what sense does it only provide minimal benefits? On which sequences?

### Soundness
1 poor

### Presentation
3 good

### Contribution
2 fair
