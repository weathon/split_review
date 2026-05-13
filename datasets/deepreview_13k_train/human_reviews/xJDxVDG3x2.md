# MolSpectra: Pre-training 3D Molecular Representation with Multi-modal Energy Spectra

- Decision: Accept
- Scores: 5, 8, 6

## Abstract
Establishing the relationship between 3D structures and the energy states of molecular systems has proven to be a promising approach for learning 3D molecular representations. However, existing methods are limited to modeling the molecular energy states from classical mechanics. This limitation results in a significant oversight of quantum mechanical effects, such as quantized (discrete) energy level structures, which offer a more accurate estimation of molecular energy and can be experimentally measured through energy spectra. In this paper, we propose to utilize the energy spectra to enhance the pre-training of 3D molecular representations (MolSpectra), thereby infusing the knowledge of quantum mechanics into the molecular representations. Specifically, we propose SpecFormer, a multi-spectrum encoder for encoding molecular spectra via masked patch reconstruction. By further aligning outputs from the 3D encoder and spectrum encoder using a contrastive objective, we enhance the 3D encoder's understanding of molecules. Evaluations on public benchmarks reveal that our pre-trained representations surpass existing methods in predicting molecular properties and modeling molecular dynamics, with an average performance improvements of 6.46%.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
Authors introduce a new data modality to the pretraining of 3d molecular structures representation models, namely absorbtion spectra in three different frequency spans: IR, UV, Raman. To encode the spectra they use transformer on top of the spectral patches with positional encoding. They use two-stage pretraining, by first denoising on a larger dataset without spectra; and then using contrastive learning objective coupled with the masked spectral patch reconstruction objective to finish pretraining. Authors demonstrate effectivnes of incorporating spectral information without denoising pretraining on QM9 dataset. Then they show small improvement in prediction quality on downstream tasks for QM9 and MD17 datasets.

### Strengths
Incorporating additional data is always useful. Although benefits are marginal, this work will be relevant for subsequent methods that learn representations of molecules. The validating experiments show that performance improvements are consistent albeit small.

### Weaknesses
1. The method of pretraining suffers from additional complexity due to two-step pretraining procedure. The choice of such pretraining schedule is not well explained.
2. Table 2, first column, methods Torch-MD and PaiNN should be bold, similarly second column there methods that perform better or on par with the proposed one.
3. Table 4 and 5 show that the method is sensitive to the parameters of the patch and stride sizes of spectrum encoder, the difference in performance in predicting homo 0.2, lumo 0.5, gap 0.2 between the closest values of these parameters. This roughly corresponds to the difference between next best performing method homo 0.5, lumo 1.5, gap 0.6. We suspect that row 1 column overlap ration the number is incorrect and should be swapped with row 3 same column. 
4. Authors mention that they fine tuned parameters such as stride/patch/mask and additionally weights of each objective. We hope that the tuning was done using pretraining dataset and not downstream tasks performance. This is not mentioned in appendix C2 or the main text. Please clarify this point.

### Questions
1. Can the model be learned in one step simultaneously with contrastive objective and denoising one? 
2. How sensitive the results are to different learning rate/transformer configuration given fixed stride/patch/mask/ optimizer parameters.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
- Unlike common approaches, the authors incorporate quantum information to enhance the quality of molecular representations.

 - The denoising component of the model is carefully designed to account for rotational and vibrational degrees of freedom in the energy.

 - The model consists of two distinct parts connected by contrastive loss: one for denoising and the other a transformer for quantum spectrums.

 - Numerous experiments demonstrate the model’s superiority over conventional methods.

The attempt to incorporate quantum information into the model is impressive. Generally, this approach is believed to enhance prediction performance over conventional models that rely on classical methods. However, as outlined in the questions section, there are still unresolved points. Therefore, the score is not final, and I am open to further discussion with the authors before finalizing it.

### Strengths
- A quantum mechanical approach is considered for molecular representation learning.

 - The denoising component of the model is designed with sophistication, incorporating both rotational and vibrational energies into the Boltzmann distribution.

 - A contrastive setting enables inference without molecular spectral data, enhancing the model's usability in real-world situations.

 - Numerous downstream experiments demonstrate that the model outperforms conventional approaches.

### Weaknesses
 - The spectral data has a high dimensionality, and the model’s transformer architecture is quite resource-intensive. Given that the contrastive loss requires numerous data combinations, the model is likely to be computationally demanding.

 - The experiments do not include comparisons with recent models, such as SliDe (1) or Frad(2), despite the model’s energy function incorporating potential forms used in both SliDe and Frad.

 - The experimental conditions are not rigorously introduced such as number of negative samples in contrastive loss and noise generation parameters.

### Questions
- The model appears computationally heavy. Is there any analysis of the computational costs for the experiments conducted?

 - Based on results from other studies, Frad and SliDe seem to perform better on QM9 and MD17 tasks. Have any additional tests been conducted to compare these recent methods?

 - If Frad and SliDe outperform the proposed model—and both already account for specific potential energy forms similar to this model—can it truly be claimed that the inclusion of quantum spectral data contributes to the model's superiority? Is there any analysis or ablation study that demonstrates the usefulness of the quantum data?

### Soundness
4

### Presentation
2

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
This paper proposes MolSpectra, an approach for pre-training 3D molecular representations by combining a denoising objective with a contrastive loss. The contrastive loss aligns the 3D representations with representations for molecular spectra (UV-Vis, IR, Raman), which are trained via a masked patch reconstruction (MPR) objective. The authors argue that incorporating information from molecular spectra enables MolSpectra to learn the dynamic evolution of molecules by understanding energy level transition patterns. MolSpectra is evaluated on the QM9 and MD17 benchmarks and compared to existing methods.

### Strengths
+ The paper presents an interesting approach to molecular representation learning by incorporating information from spectra.

+ The motivation for incorporating spectral data is well-justified. The authors argue that quantized energy levels are fundamental to understanding molecular properties and dynamics, and that spectral data provides a direct measurement of these levels.

+ The proposed SpecFormer architecture and the associated MPR and contrastive learning objectives are technically sound and well-designed.

### Weaknesses
 - The results on the QM9 and MD17 benchmarks presented in Tables 2 and 3 are misleading for two reasons: (1) In Table 2 (QM9), the caption states that the best results are highlighted in bold, however, this is not true. In fact, the numbers for MolSpectra are highlighted in bold for 9 out of 12 columns, but it only achieves the best results in 3 out of 12 columns. (2) Both tables only include older models that are not SOTA anymore. Newer models such as MACE (https://proceedings.neurips.cc/paper_files/paper/2022/file/4a36c3c51af11ed9f34615b81edb5bbc-Paper-Conference.pdf) and Allegro (https://www.nature.com/articles/s41467-023-36329-y) achieve significantly better results than all listed models (I have not done a literature search to check which model is the current SOTA, those are just two models with better performance I know at the top of my head).
The authors should include results for more recent (SOTA) models in both tables and fix the formatting, so that the result that is actually best is highlighted in bold. In addition (this is a minor suggestion that does not affect my rating), I think it would be helpful to readers to include (either in the caption, or within the table itself) an explanation/label what the horizontal separator signifies. I assume this is to distinguish models trained from scratch from models that were pre-trained in an unsupervised manner and then finetuned, but this should probably be made explicit.

- It is difficult to assess how big the improvement of including spectral information into the unsupervised representation learning actually is. This is because it is not immediately clear from Tables 1 and 2 how the same model architecture, (pre-)trained on the same structural data, performs when the *only* difference is whether spectral information was included in pre-training or not. The authors write on p.7 that Coord serves as primary baseline, but it is not clear from the text whether this is actually the same model architecture, and how exactly it was trained. To have an objective baseline, I suggest to pre-train the same architecture using the two-stage pre-training pipeline (section 3.4) twice, with the only difference being that $\beta_{\text{MPR}}$ and $\beta_{\text{Contrast}}$ are set to zero for one of the models. This way, the only difference is whether spectral information is used or not, allowing a direct assessment of the effectiveness of including this information.

- The manuscript applies MolSpectra only to a single architecture for structural representation learning (TorchMD-Net). It is therefore difficult to judge whether MolSpectra is generally effective, or whether its usefulness is strongly dependent on the underlying architecture used for structural representation learning. To address this shortcoming, the authors should apply MolSpectra to pre-training other architectures (ideally using the method described in my previous point to establish objective baselines for each architecture). This would allow readers to assess MolSpectra in a broader context and would significantly strengthen the paper.

- The authors state that "MolSpectra learns the dynamic evolution of molecules by understanding energy level transition patterns", however, this statement is not supported by direct evidence. I think it is a valid hypothesis, but it should be tested explicitly. Fortunately, a very direct test is possible: As the authors correctly state, the denoising objective is equivalent to learning a force field. This means that models trained with/without MolSpectra on a denoising task can be directly used as a force field to run molecular dynamics (MD) simulations. From such MD simulations, it is trivial to extract the power spectrum of a molecule via the velocity autocorrelation function (see e.g. https://doi.org/10.1039/C3CP44302G if the underlying theory is not familiar). The power spectrum contains the same peaks as the IR and Raman spectra, with the only differences being that (1) all internal vibrations are active (in contrast to IR/Raman spectra, where only some vibrations are visible - the power spectrum contains peaks from both!) and (2) the peak intensities are different. The peak positions, however, are directly comparable. If the spectral information actually teaches a model about the dynamics of a molecule, I would expect the power spectrum of a model trained with MolSpectra to show much better agreement (in peak positions) to the "ground-truth" IR/Raman spectra. The authors should perform this test, as it would make the paper much more insightful.

- In section 2.2, the authors describe three different energy functions that can be used for pre-training. It is not immediately clear from the text which of these is actually used for MolSpectra. From context, I assume it is variant I, but I think stating this explicitly would make it easier to understand the details of the method.

- The paper lacks an analysis of the computational complexity and resource requirements of the proposed method. A comparison of training time and resource usage with baseline methods would be beneficial.

- While the ablation study provides insights into the importance of the MPR objective, a more comprehensive ablation study is needed to assess the individual contributions of different spectral modalities (UV-Vis, IR, Raman). This would provide a deeper understanding of how each component contributes to the overall performance.

- The paper mainly compares against methods that rely on 3D structure information only. Comparison with other multimodal methods for molecular representation learning would provide a more complete picture of MolSpectra's performance relative to other methods.

### Questions
* From the appendix, it seems like TorchMD-Net is the model used for structural representation learning. Is the architecture in any way different to the TorchMD-Net model for which results are reported in Tables 2 and 3? If yes, these differences should be pointed out explicitly. Also, I suggest relabelling the entries for MolSpectra in Tables 2 and 3 as something like "TorchMD-Net (w/ MolSpectra)" or similar. Also, the baseline (see my suggestions above) should be clearly labelled as such, so that readers know which numbers to compare to.

* Could the authors elaborate on the choice of the specific spectra types (UV-Vis, IR, and Raman) used in this work? It seems to me like other types of spectra, such as NMR and mass spectra, could provide additional information and further enhance the learned representations.

* Can the authors provide details on the computational complexity and resource requirements of MolSpectra, including training time and memory usage? A comparison with baseline methods would be helpful.

* How does the performance of MolSpectra scale with the size and diversity of the molecular dataset used for pre-training?

* Can the authors provide a more in-depth analysis of the learned representations? For instance, visualizing the latent space or analyzing the attention patterns in SpecFormer could provide insights into the captured features and relationships.

* For the simple test of the effectiveness of molecular spectra (section 4.1/Table 1), where do the spectra used to obtain the spectral representations come from? I assume they are taken from QM9S, but this should be stated explicitly.

* How sensitive is MolSpectra to the choice of hyperparameters in Eq.8 ($\beta_{\text{Denoising}}$, $\beta_{\text{MPR}}$, and $\beta_{\text{Contrast}}$)? The authors mention in the appendix that they tuned these hyperparameters by trying different values. I believe the results for these different runs should also be included (in the appendix is fine), so readers can develop an intuition how changes to the values affect down-stream performance.

* In the appendix, the authors write that they apply a $\log_{10}$ transform to the peak intensities to mitigate interference causes by peak intensity differences. It seems intuitively more meaningful to me to instead normalize spectra by setting the height of the highest intensity peak to an arbitrary value (say 1) and scaling the remaining peaks proportionally. Have the authors experimented with different "normalization procedures" such as the one mentioned?

**Additional Feedback:**

* A discussion of the limitations of the proposed method and potential future directions for research would be interesting.

* There is a typo on p.8 l.427/428: "yiels" should be "yields".

### Soundness
1

### Presentation
2

### Contribution
2
