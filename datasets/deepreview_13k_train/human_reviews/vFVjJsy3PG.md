# Geometric Representation Condition Improves Equivariant Molecule Generation

- Decision: Reject
- Scores: 6, 5, 5, 3, 8

## Abstract
Recent advancements in molecular generative models have demonstrated substantial potential in accelerating scientific discovery, particularly in drug design. However, these models often face challenges in generating high-quality molecules, especially in conditional scenarios where specific molecular properties must be satisfied. In this work, we introduce GeoRCG, a general framework to enhance the performance of molecular generative models by integrating geometric representation conditions. We decompose the molecule generation process into two stages: first, generating an informative geometric representation; second, generating a molecule conditioned on the representation. Compared to directly generating a molecule, the relatively easy-to-generate representation in the first-stage guides the second-stage generation to reach a high-quality molecule in a more goal-oriented and much faster way. Leveraging EDM as the base generator, we observe significant quality improvements in unconditional molecule generation on the widely-used QM9 and GEOM-DRUG datasets. More notably, in the challenging conditional molecular generation task, our framework achieves an average 31\% performance improvement over state-of-the-art approaches, highlighting the superiority of conditioning on semantically rich geometric representations over conditioning on individual property values as in previous approaches. Furthermore, we show that, with such representation guidance, the number of diffusion steps can be reduced to as small as 100 while maintaining superior generation quality than that achieved with 1,000 steps, thereby significantly accelerating the generation process.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper, titled "Geometric Representation Condition Improves Equivariant Molecule Generation" (GeoRCG), presents a novel approach to improving molecular generative models by incorporating geometric representation conditions. The GeoRCG framework divides the molecule generation process into two stages: first, generating an informative geometric representation; second, generating a molecule conditioned on this representation.

The core idea is to first generate a compact geometric representation of a molecule using a pre-trained geometric encoder. This representation captures essential information about molecular structure without the complexity associated with 3D symmetries, making the generation task simpler and more effective. Leveraging this representation, the second stage uses a molecule generator to produce the final molecule. The framework employs EDM as the base generator and shows significant improvements in both unconditional and conditional molecule generation tasks. Specifically, GeoRCG achieves an average 31% performance gain over state-of-the-art methods on challenging conditional generation tasks.

### Strengths
The key strength of GeoRCG lies in its innovative use of geometric representations to condition molecular generation. By transforming the generation problem into a two-stage process—first generating a geometric representation and then generating the molecule conditioned on this representation—the paper introduces an effective way to simplify the complex task of molecular generation. This approach addresses major challenges like handling 3D geometric symmetries and provides a significant improvement over existing methods that attempt to directly learn molecular distributions.

The clear and structured presentation of the methodology, supported by well-executed empirical evaluations and visual explanations, adds to the clarity and accessibility of the paper. GeoRCG's advancements could have a significant impact on drug discovery and material design, highlighting its importance for both research and practical applications.

### Weaknesses
While the paper emphasizes the use of geometric representations to simplify the generation task, there is insufficient analysis of how different pre-trained encoders impact the overall quality of the generated molecules. The choice of pre-trained encoders (UniMol and Frad) is central to the approach, but the authors do not explore how variations in the pre-training dataset or encoder architecture affect the representations. Conducting a more comprehensive analysis, such as comparing multiple pre-trained models trained on different datasets, different architectures (e.g., graph neural networks vs. transformers), or even different pre-training objectives (e.g., contrastive learning vs. masked language modeling), would help clarify the impact of representation quality and improve confidence in the method’s robustness. For example, it would be useful to see if encoders trained on datasets with more diverse chemical structures lead to better performance on a wide range of molecular generation tasks.

The representation generator aims to remove symmetries such as O(3) and S(N), but the impact of symmetry removal on downstream tasks is not thoroughly analyzed. Specifically, it would be beneficial to explore whether there are specific symmetries that contribute positively to certain molecular properties or whether removing all symmetries has unintended negative effects on some downstream applications. For example, certain chiral properties are inherently linked to 3D symmetry, and it is unclear if removing the O(3) symmetry will impact the model's ability to generate molecules with specific chiral properties. Conducting ablation studies that selectively preserve certain symmetry properties, perhaps by using equivariant layers in the representation generator or by conditioning on symmetry-related features, could offer insights into how symmetry affects molecule generation and provide a more nuanced understanding of its role.

In the conditional generation setting, the paper discusses training the representation generator on (molecule, property) pairs. However, this strategy is limited to simple properties like HOMO-LUMO gap, polarizability, etc., and there is no clear extension for complex properties such as molecular binding affinity or ADMET (Absorption, Distribution, Metabolism, Excretion, and Toxicity) properties. Such properties typically require more context or knowledge beyond geometric structure alone. For instance, binding affinity is heavily influenced by interactions with a protein target, which is not captured by the geometric representation of the molecule alone. Addressing this limitation, either by discussing possible extensions or incorporating more sophisticated conditioning mechanisms (e.g., using multi-modal data such as 3D structure and protein targets, or incorporating knowledge graphs that encode chemical and biological information), would make GeoRCG more applicable to real-world drug discovery problems.

### Questions
See weakness

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper presents a theoretical foundation and specific implementation of latent diffusion for molecular generation. Instead of directly operating with molecular graphs (e.g., continuous Euclidean coordinates and categorical atom types), the method proposes projecting molecules into a latent space and using latent representations that are O(3) and SO(3) invariant. Diffusion is performed in this simplified latent space, and then the molecules are reprojected to predict their structures. This approach reduces computational costs, resulting in a denoising neural network that is much smaller and simpler, as well as reducing the number of steps required for diffusion.

### Strengths
Improved Speed through Latent Diffusion: Latent diffusion has great potential to enhance the speed of 3D molecule generation. In this paper, the authors demonstrated that they were able to reduce the number of diffusion steps from the commonly used 1000 or 500 to just 100 without any performance drop. Performing diffusion in a simpler latent representation appears to be a highly effective approach.

Better Bond Length and Angle Distributions on QM9 Dataset: The proposed model generates bond length and bond angle distributions that more closely resemble those of the QM9 dataset. This is a reasonable metric for assessing the quality of generated 3D structures and indicates an improvement over previous methods.

### Weaknesses
Limited 3D Metrics on Larger Datasets: The only reported 3D metric for the more realistic and larger GEOM Drugs dataset is atom stability. Since the atom stability is only 0.86 for GEOM Drugs itself, this raises questions about the reliability of the metric. A more comprehensive and accurate comparison is required to fully assess the model’s performance on larger datasets. Specifically, metrics such as the distribution of bond lengths and angles, which are crucial for assessing the quality of generated 3D structures, are missing. The absence of these metrics makes it difficult to ascertain whether the model is truly generating realistic molecular geometries on larger datasets.

Overlooking Models That Do Not Rely on External Software: The paper states that models such as MiDi and LDM3DG use domain knowledge through Open Babel, which gives them advantages. However, there are models like JODO, EQGATDiff, and SemlaFlow that directly predict bonds without relying on external software. Including these models in comparisons would provide a more comprehensive evaluation and highlight the strengths and weaknesses of the proposed method. The lack of comparison with these models leaves a gap in understanding the relative performance of the proposed method in the context of methods that learn bond formation directly.

Questionable Reliance on Lookup Tables: The reliance on a lookup table for bond lengths is questionable. Depending on the molecular configuration and the specific energy calculation method used (which is GFN2-xTB for GEOM Drugs), bond lengths can vary within a 10% interval. This variability suggests that a static lookup table may not accurately capture the nuances of bond lengths across different molecules. This approach may lead to inaccuracies in the generated structures, especially for molecules with complex bonding environments.

Lack of Comparison with Faster Models: While the method aims for faster molecule generation by reducing the number of diffusion steps, previous models have already utilized flow matching to reduce steps to 200 (EquiFM) or even 20 (SemlaFlow). Including these models in the comparison would strengthen the research by providing context for the improvements and demonstrating how the proposed method stands relative to existing fast-generation techniques. Without this comparison, it's difficult to assess the true speed advantage of the proposed method compared to other state-of-the-art fast generation techniques.

### Questions
Could you add bond length and bond angle metric comparisons for the GEOM Drugs dataset? Providing these metrics would offer a more complete evaluation of the model’s performance on larger and more complex datasets.

Would you consider comparing your model with others like JODO, EQGATDiff, or SemlaFlow, which generate the full graph including bonds? A comparison with these models, especially SemlaFlow due to its speed and reduced number of steps, could be particularly beneficial in highlighting the advantages and limitations of your approach.

In the paper, there is no reference to the GEOM paper, and there is a claim: “Crucially, many structures in GEOM-DRUG lack the equilibrium conditions necessary for pre-training methods that enable effective learning of force fields,” which could be misleading. All GEOM Drugs molecules have optimized geometries with respect to GFN2-xTB energy calculations. Could you reconsider this statement? Clarifying this point and accurately referencing the GEOM dataset would enhance the credibility and accuracy of your pape

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper introduces an intermediate representation approach to find better property conditioning for molecular generation. The authors show success for properties such as polarizability (\alpha) over the QM9 data set, but other state-of-the-art models outperform the model on the more extensive dataset DRUG.

### Strengths
This paper is well-written and easy to read. The authors present their results clearly and clearly, and the method is also well described.

### Weaknesses
The main weakness of this approach is that the performance in the DRUG dataset does not beat SOTA. QM9 is a great research-level dataset for small molecules, but DRUG is industrially relevant and has more realistic molecules. The paper's reliance on an intermediate representation, while novel, does not seem to translate to superior performance on larger, more complex molecules. Specifically, the method's performance on the DRUG dataset, which includes molecules with a wider range of sizes and chemical functionalities, lags behind existing state-of-the-art models. This indicates a potential limitation in the method's ability to generalize beyond the relatively simple chemical space of the QM9 dataset. The lack of a clear advantage on the DRUG dataset raises concerns about the practical applicability of the proposed method for real-world drug discovery scenarios.

### Questions
Is it possible to get (during revisions) a more extensive effort to match or exceed SOTA for the DRUG dataset? This would raise my reviewer score. At the moment, I think this paper is a  technical but not revolutionary improvement and may belong to a journal or another venue rather than ICLR. If the improvement over larger molecules is demonstrated, I think it may be more of interest to this community.

### Soundness
4

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
4

### Summary
The authors introduce GeoRCG, a general framework to enhance conditional molecule generative models by including geometric representations. GeoRCG splits the generation process into two parts the first being to create an informative geometric representation followed by generating a molecule conditioned on this representation. Using GeoRCG they can improve upon base EDM for QM9 and GEOM-DRUGs datasets, reducing the number of inference steps from 1000 to 100.

### Strengths
- Overall GeoRCG demonstrates how leveraging powerful pretrained molecule representations to condition generative models can improve results for QM9 molecules.
- Strong evidence shows that guidance mixed with low-temperature sampling improves QM9 results in Figure 4.
- By conditioning the cheap representation generator on the property of interest it pushes the complexity of conditional generation to be more managible.

### Weaknesses
 - There is an overemphasis on QM9 in the benchmarks, with little attention to the more challenging GEOM DRUGS which more accurately represents drug-like molecules. Molecule stability, connectivity, and other metrics are included in MIDI but have not been reported. This is important, especially for a method that demonstrates improvement over base EDM for QM9, since for Drugs EDM obtains only 5.5% molecule stability and 40.3% after OpenBabel (numbers taken from MIDI).
  Connectivity is not reported for any method, which is important for 3D molecule generation. If the molecule is not connected, RDKit can often still parse it, but it is not a single-molecule structure. From MIDI EDM + OpenBabel, the result is only 41.4%, which is quite low.

Overall, it's hard to understand what is translatable as a general method for other biological tasks since QM9 is a toy task.

### Questions
- How does low-temperature sampling impact prior DRUGS baselines, as it is used in Table 1? Methods mentioned, such as Chroma, suggest that it can have a significant impact.
- How does this same method apply to other models beyond EDM given it is a general framework?
- How does the performance vary as a function of sampling steps for DRUGs and their respective benchmarks?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper introduces a novel framework to improve 3D molecular generation by integrating certain geometric representation conditions into the molecular generation process, and then conditioning on these representations to generate a molecule.

### Strengths
Good background, appreciate the previous work review in the appendix.

Appreciate the heat maps in Figure 4, good demonstration of these parameters allowing a scientist to specify the tradeoff between properties depending on application.

### Weaknesses
There are no glaring weaknesses of this paper. All choices made have been clearly communicated and motivated. Important limitations of the method are clearly outlined in the Conclusions section of the paper.

Small change, but please change the colors used in the tables for red/green colorblind readers.

### Questions
- Please define EDM in your abstract.
- The writers vaguely refer to the improved “quality” of the generated molecules as the first achievement of this method. This is too vague—what does quality mean here?  
- Again, the second bullet talks about model performance, citing a 31% increase. What is this “performance”? Please cite the metric and the benchmark here.
- Last bullet—reduce the number of diffusion steps by what percent on average? Please be specific here at this point in the paper.

### Soundness
3

### Presentation
3

### Contribution
4
