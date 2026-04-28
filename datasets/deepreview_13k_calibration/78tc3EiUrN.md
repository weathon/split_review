# MADGEN - Mass-Spec attends to De Novo Molecular generation

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6, 6

## Abstract
The annotation (assigning structural chemical identities) of MS/MS spectra remains a significant challenge due to the enormous molecular diversity in biological samples and the limited scope of reference databases.  Currently, the vast majority of spectral measurements remain in the "dark chemical space" without structural annotations.  To improve annotation, we propose MADGEN (Mass-spec Attends to De Novo Molecular GENeration), a scaffold-based method for de novo molecular structure generation guided by mass spectrometry data. MADGEN operates in two stages: scaffold retrieval and spectra-conditioned molecular generation starting with the scaffold. In the first stage, given an MS/MS spectrum, we formulate scaffold retrieval as a ranking problem and employ contrastive learning to align mass spectra with candidate molecular scaffolds. In the second stage, starting from the retrieved scaffold, we employ the MS/MS spectrum to guide an attention-based generative model to generate the final molecule. Our approach constrains the molecular generation search space, reducing its complexity and improving generation accuracy. We evaluate MADGEN on three datasets (NIST23, CANOPUS, and MassSpecGym) and  evaluate MADGEN's performance with a predictive scaffold retriever and with an oracle retriever. We demonstrate the effectiveness of using  attention to integrate spectral information throughout the generation process to achieve strong results with the oracle retriever.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This study presents MADGEN, a two-stage framework for generating molecular structures from MS/MS data. In the first stage, MADGEN retrieves a scaffold using either predictive retrieval or oracle retrieval. In predictive retrieval, MADGEN treats scaffold selection as a ranking task, using contrastive learning to align embeddings of mass spectra and scaffold candidates in a shared latent space, scoring each scaffold to identify the best match. Oracle retrieval, by contrast, directly uses RDKit to extract the correct scaffold from a molecular graph. In the second stage, starting from the retrieved scaffold, MADGEN generates the full molecular structure through a Markov bridge-based expansion, sequentially adding atoms and bonds with classifier-free guidance to integrate spectral information. Evaluations were performed on datasets NIST23, CANOPUS, and MassSpecGym, underscoring its potential in metabolomics and drug discovery applications.

### Strengths
* The two-stage idea is interesting.
* The oracle retrieval method is more effective.

### Weaknesses
 * The SPA of the predictive retrieval is very low.
* The predictive retrieval approach yields poor molecule generation in Phase 2, where the generated structures fail to align with target properties, underscoring a critical limitation.
* The conditioning of molecular generation on mass spectrometry data is largely based on classifier-free guidance, a well-established technique. The novelty is not well articulated.
* The absorbing transition matrix only applies to isolated atoms, strictly enforcing scaffold structure. This hard constraint could be problematic, especially when the chosen scaffold is incorrect, potentially limiting the model's ability to correct errors in the scaffold retrieval stage.
* The contrastive learning approach for aligning mass spectra and molecule embeddings lacks detailed explanation, making it difficult to assess its effectiveness and potential limitations. The method's reliance on a CLIP-like framework, while established, needs more specific details on how the embeddings are generated and aligned in this particular context.

### Questions
* How is the candidate scaffold pool determined for predictive retrieval? There can be a huge number of scaffold candidates.
* How does the contrast learning work for aligning the embeddings of mass spectra with their corresponding molecule? Some explanations are needed. 
* Regarding molecular generation in Phase 2, the absorbing transition matrix only applies to isolated atoms, strictly enforcing scaffold structure. Will such a hard constraint be problematic especially when the chosen scaffold is incorrect?
* Oracle retrieval requires both the MS/MS spectrum and the chemical formula (molecular graphs). If chemical formula is known, what are the remaining challenging in solving the molecular structures?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper introduces MADGEN, a method for de novo molecular generation using mass spectrometry data. MADGEN simplifies the structure generation process by retrieving molecular scaffolds and building complete molecules upon them. The experimental results on three datasets demonstrate that MADGEN can effectively generate accurate molecular structures when the scaffold is known.

### Strengths
- The use of scaffolds for simplifying molecular generation is a novel and effective strategy that reduces complexity.
- The paper is clear and easy to understand.

### Weaknesses
 - The method lacks a comparison with other baselines.

### Questions
- I would appreciate it if you could include a comparison of MADGEN with other prediction methods.

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
The paper introduces MADGEN, a framework for de novo molecular structure generation from mass spectrometry data. MADGEN employs a two-stage approach: first, it retrieves a molecular scaffold, and second, it completes the molecule conditioned on both the scaffold and the MS/MS spectra. Evaluated on datasets like NIST23, CANOPUS, and MassSpecGym, MADGEN effectively reduces search complexity and enhances accuracy.

### Strengths
1. The two-stage approach of scaffold retrieval followed by scaffold-conditioned molecular generation presents a novel solution for de novo molecular structure prediction.
2. The paper is well-written and easy to follow.
3. The model is evaluated on multiple datasets, and a detailed ablation study is provided.

### Weaknesses
1. The scaffold retrieval performance, especially when using a predictive retriever, remains relatively low (e.g., NIST23). The reported Top-1 accuracy of 1.8% and similarity of 0.06 on NIST23 suggests that the predictive retriever struggles to identify the correct scaffold. This significantly limits the potential of the subsequent molecular generation stage, as the model is conditioned on a potentially incorrect scaffold.
2. The discussion of baselines is unclear. The paper lacks a comprehensive comparison to existing state-of-the-art methods, making it difficult to assess the true novelty and performance of MADGEN. The absence of clear baseline performance metrics for all datasets hinders the evaluation of the proposed approach relative to established techniques.

### Questions
1. In Section 3.2.1, the authors state, “Since the atom set V can be directly inferred from the chemical formula.” However, it is unclear where the chemical formula is derived from. Could the authors clarify this, as in real-world scenarios, the input typically does not contain the chemical formula?
2. For the MassSpecGym dataset, what is the “best published state-of-the-art performance” referred to? Are there baseline performance metrics reported for the other two datasets as well?

### Soundness
3

### Presentation
4

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
The paper presents MADGEN, a method for de novo molecular structure generation using MS/MS data to address challenges in spectral annotation. MADGEN operates in two stages: scaffold retrieval via contrastive learning and attention-based generation using the MS/MS spectrum. Evaluated on NIST23, CANOPUS, and MassSpecGym datasets, MADGEN shows strong performance, particularly with an oracle retriever, improving annotation by leveraging spectral data effectively.

### Strengths
1. The task of de novo generation of molecular structure from mass spectrum is important and challenging.  However, the AI community has not paid enough attention to this task.       
2. The two-stage molecule structure generation method is novel.

### Weaknesses
1. The authors have not compared with previous de novo molecular elucidation methods from MS such as MSNovelist [1], Spec2Mol [2], MIST [3], etc.
2. manuscript’s presentation requires significant improvement for publication readiness:
    (1) Line 14 - Line 50: Double quotation marks should be directional.            
    (2) Line 242 - Line 243: Why the word 'Following' is underlined?       
    (3) Why there is $T$ in Eq. (6)?              
    (4) \citep is used for parenthetical citations while \citet is used for textual citations, where the citation is part of the sentence. The authors are suggested to use these two commands appropriately to ensure clarity in their references and maintain consistency in citation formatting.             
    (5) Line 102: The “F” in “Generative Frameworks for molecular generation” should be lowercase.             
3. The code is not provided for reproducing the results.

### Questions
See the weakness above.

### Soundness
3

### Presentation
3

### Contribution
3
