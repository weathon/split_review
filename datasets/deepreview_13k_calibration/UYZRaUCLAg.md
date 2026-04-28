# Solving Inverse Problems in Protein Space Using Diffusion-Based Priors

- Decision: Reject
- Avg Score: 5.33
- Scores: 5, 3, 8

## Abstract
The interaction of a protein with its environment can be understood and controlled via its 3D structure. Experimental methods for protein structure determination, such as X-ray crystallography or cryogenic electron microscopy, shed light on biological processes but introduce challenging inverse problems. Learning-based approaches have emerged as accurate and efficient methods to solve these inverse problems for 3D structure determination, but are specialized for a predefined type of measurement. Here, we introduce a versatile framework to turn raw biophysical measurements of varying types into 3D atomic models. Our method combines a physics-based forward model of the measurement process with a pretrained generative model providing a task-agnostic, data-driven prior. Our method outperforms posterior sampling baselines on both linear and non-linear inverse problems. In particular, it is the first diffusion-based method for refining atomic models from cryo-EM density maps.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper introduced a framework, ADP-3D, which uses a diffusion model as a prior to solve the inverse problem in structural biology. The authors leverage the pretrained diffusion models in the atomic model space like Chroma and RFDiffusion as their prior. The downstream tasks include structure completion (as a toy problem), atomic model refinement (model completion given a simulated density map, an incomplete atomic model, and the sequence), and solving structure from given pairwise distances.

### Strengths
As far as my knowledge goes, this work is one of the first to leverage a pretrained diffusion model of protein atomic structures as a Bayes prior, to solve the inverse problems which are very common in structural biology. The connection between the generative model and the experimental observation is very important in expanding the scope of the AI for science field.

### Weaknesses
1. Since the paper uses pretrained diffusion models from Chroma and RFDiffusion, and the measurement models for the tasks are apparent, from a methodological standpoint, my understanding is that the main contribution of this paper is the MAP estimation method given a diffusion prior. As ADP-3D seems like a generic algorithm that is not heavily tailored for structural biology, there are many similar methods in the field of diffusion posterior sampling for inverse problems, e.g. DPS, $\Pi$GDM, as surveyed in [1] and also mentioned in the related work section by the authors. The authors should compare the similarities and differences between the propose ADP-3D method and other similar algorithms. The authors should also use at least one of these methods as the baseline and compare the results to show the advantage of the proposed ADP-3D method.

2. I understand that real data is not considered in the scope of this paper, but this makes the downstream tasks a bit far from the real world implementation. For example, the model refinement task uses a small, simulated density as a given condition, while ModelAngelo itself was trained on real experimental density maps. In reality, it is possible that ModelAngelo does not even output a severely incomplete model, making the whole setting of this task futile.

3. The model refinement task seems to only contain one example (7pzt).

### Questions
1. How does ADP-3D related and differ from other diffusion posterior sampling methods?

2. In the model refinement task, what happens if using an experimental density map as the condition? The authors claimed that "most cryo-EM-resolved models are incomplete", but in my opinion the authors should at least have one more realistic case to show the setting in this task is not a castle in the air.

### Soundness
2

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
4

### Summary
The paper introduces ADP-3D (Atomic Denoising Prior for 3D reconstruction), an algorithm to combine a pretrained protein diffusion model with additional data. The method uses a plug-n-play approach that splits the log posterior into a prior and likelihood term, duplicates the variables and couples them via a quadratic term. This allows the authors to avoid incorporating the likelihood directly into the diffusion process. Instead only a simple quadratic term needs to be added to the likelihood, and a diffusion step is used to incorporate the prior. No retraining of the diffusion model is necessary. The authors focus on the Chroma model (Ingraham et al., 2023) for protein structures and combine the model with various likelihoods (structure completion from sub-sampled backbone positions, model refinement based on a density map, sequence information, incomplete distance matrix). Using specific examples, the authors find that the incorporation of the diffusion process improves the quality of the reconstructed structures.

### Strengths
* A general approach to combining pretrained diffusion models with data based on a variable-splitting framework.
* The resulting algorithm is quite simple and allows for combining pretrained diffusion models with new data (thereby avoiding a retraining step).
* The approach is illustrated for various protein structure modeling tasks.

### Weaknesses
 * The general approach (algorithm 1) seems to be a minor modification of existing work.
* The method is illustrated only for simulated data.

__Recommendation__

I recommend to reject the article. ADP-3D is a straight forward application of the plug-n-play framework to protein diffusion models. The idea of using a variable splitting approach to combine diffusion models with additional data has already been proposed by Zhu et al. (2023) in the context of image restoration. So the major novelty is in the application of the method to protein structure modeling. However, the authors only use simulated data in their numerical experiments.

### Questions
* The abstract states that this is "the first diffusion-based method for refining atomic models from simulated cryo-EM maps." Why did you not apply the method to real cryo-EM maps? The paper would be much stronger, if you showed applications to real data. Likewise, you could use NMR distance bounds as experimental distance information rather than simulated distances. 
* How do you choose the parameter $\rho$? Are the results sensitive to the choice of $\rho$? 
* How do you define __completeness__? You state that completeness is the "RMSD of the predicted structure for the X% most well-resolved alpha carbons (compared to the deposited structure)." How do you assess if an alpha carbon is well-resolved? Please note that the resolution of your model (in my understanding something like its precision) and its accuracy are not the same thing. 
* Figures 3, 4, 5 report the resolution of the deposited structure. What is the purpose of showing this number? The resolution of the PDB structure does not tell us anything about the difficulty of the structure calculation task.
* Figure 5, right panel: Why does the RMSD increase with increasing number of distances (#pd > 4k) when not using a diffusion model? It should go down and should also approach zero for as many distances as 8 k pairwise distances for a protein of length 127 residues.

__Additional feedback__

* The selection of distances is unrealistic in the sense that, for example, NMR experiments such as NOESY only probe short distances up to 6 \AA. Since there are many more long-range distances, your way of selecting distances randomly will tend to pick distances that are not experimentally accessible, which makes the selection process unrealistic. 
* The abstract states that "raw biophysical measurements such as cryo-EM density maps" can be used by your method. To categorize cryo-EM maps as raw data is misleading. A density map is the result of a complex sequence of processing steps starting with motion correction, particle picking, etc. The raw measurements in cryo-EM are the micrographs. 
* Figure 1 does not add much information beyond what is already said in the text. You could remove the figure and use the space to show more details about your numerical experiments such as your tests with RFdiffusion (Watson et al., 2023). 
* Likewise, figure 2 is a specific result for the correlation matrix used by Chroma. It could be moved to the supplementary information. 
* On page 8 you state that you avoid testing on structures that were part of the Chroma training set by using only structures that were published after the release of Chroma. However, this does not guarantee that the Chroma training set and your test structure do not overlap. First, many examples of structures of one and the same protein (or a protein with a highly similar sequence) can be found in the PDB. Second, protein structures are much more persistent than sequences. So even proteins with a low sequence similarity can have similar structures. 
* In the captions of figure 3 and 5, you report the lowest RMSD obtained with 8 runs. Please also report the maximum RMSD (you could also report the mean and the standard deviation) to give an indication of how much your models vary. 
* There is a slight inconsistency in your whole approach: You claim to do MAP estimation, but then you use diffusion-based sampling.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
- The authors propose to use a plug-and-play framework for diffusion models to inverse problems for determining protein structure
- This allows the authors to use off-the-shelf diffusion models such as Chroma to regularise these inverse problems
- The upshot is that this line of work is task-agnostic
- The authors showcase how their method yields promising results for three inverse problems: structure estimation from an incomplete structure, structure estimation from Cryo-EM 3D maps, and structure estimation from incomplete sparse pairwise distance data

### Strengths
- It is very impressive to see the results for all three inverse problems. Some aspects that are highlights to me:
    - In the structure completion it is great that the authors also test this for different levels of incompleteness. For these methods, it is good to showcase limitations to the reader
    - I am very impressed by outperforming ModelAngelo, which is as the authors mention (and to the best of my knowledge) the state-of-the-art in model building. Being able to refine the predictions to the extent in the paper is very impressive

### Weaknesses
 - The writing can be improved upon. In particular, the introduction and the related work could really benefit from restructuring and adding additional material. This would benefit the overall flow of the paper and provide the reader with a clearer overview of the problems being tackled in the paper. Detailed suggestions below:
    - Regarding the introduction:
        - Please allow me to paraphrase:
            - Paragraph 1: Proteins can be inferred in different ways through solving an inverse problem
            - Paragraph 2: Deep learning has been key take the next step, but are limited by their way of training (new problem setting, train again to the new setting)
            - Paragraph 3: Inverse problems are dominated by learned priors
            - Paragraph 4: Diffusion models are used in the field of biology
            - Paragraph 5: Our contribution to overcome the hurdle from the second paragrap is to use diffusion models
        - I would suggest a rewrite that would look as follows (high-level)
            - The order Paragraph 1, Paragraph 3, Paragraph 2, Paragraph 5 would be more natural to me. 
            - Paragraph 4 does not really serve any purpose and for me disrupts the flow of the introduction. So I would recommend removing it from the introduction and maybe move it to the background 
    - Regarding related work: 
        - I would expect that there would be something on finding structures from partial measurements and sparse distance matrices as well. Now there is just a lot on model building methods from Cryo-EM density maps
        - I would suggest to talk less about protein diffusion models, which seems more like something for the the background (I feel that there is not really a reason of spending a lot of time on it here)

 - The idea of using the score as a denoiser is not clearly attributed. The authors do not cite the works referred to in paragraph 3 of the introduction, which is problematic. The connection to existing work is not well established, making it hard to assess the novelty of the approach.
- The sentence “In particular, it is the first diffusion-based method for refining atomic models from simulated cryo-EM maps.” at the end of the abstract is confusing. It's unclear if the method has been applied to the other two inverse problems, and the focus on Cryo-EM might be misleading if the method is more broadly applicable. The abstract should be more precise about the scope of the method.

- p.1, l.28: The paragraph's opening sentence is not the most effective way to introduce the topic. Starting with the second sentence, which discusses experimental methods, would provide a more immediate and clear context for the reader. The first sentence can be used later to motivate the experiments, but it is not a good starting point.
- p.1. l.37: The claim that “These approaches can estimate the uncertainty of their answers and provide theoretical guarantees of correctness, …” is overstated. There is limited theoretical backing for the convergence of iterative methods used in this field, and the statement gives a false impression of the theoretical rigor of these methods.
- In section 2, the authors mainly focus on ModelAngelo. It would be beneficial to discuss the broader problem of model building from cryo-EM maps, rather than focusing on a single method. This would provide a more comprehensive view of the field.
- p.2 l.90: The second bullet point in the contributions claims to compare to sampling methods, but the experiments only discuss one method. This should be changed to singular, as only one method is discussed.
- Section 4.3: It is odd to have a whole section dedicated to model building from Cryo-EM maps, while the other inverse problems are defined in the experiments section. It would be more logical to have a dedicated section that introduces all three inverse problems before the experiments. This would improve clarity and make it easier for readers interested in a specific application to find the relevant information.
- p.7 l.360: The jump from the left-hand side to the right-hand side of equation 13 is too large for the reader. The intermediate steps should be explicitly written out to ensure clarity.
- p.8 l.409. typo: evalute -> evaluate
- p.9 l.458. The sentence “Note that we do not chose a structure that was resolved with cryo-EM because most cryo-EM-resolved models are incomplete.” is unclear and requires further explanation. Also, there is a typo: chose -> choose

### Questions
Questions for clarification 
- Is the idea of using the score as a denoiser yours or is this something that is commonly used in the inverse problems field? You don’t seem to cite the works referred to in paragraph 3 of the introduction.
- On that note, what confuses me is the sentence “In particular, it is the first diffusion-based method for refining atomic models from simulated cryo-EM maps.” at the end of the abstract. Has it been used for the other two inverse problems? It would be great if the authors can be more precise here. (I assume that Cryo-EM is mentioned as it is potentially the most high-impact application, but it would be good to be clear about the other problems as well)

Additional feedback
- p.1, l.28: I would not start this paragraph with this sentence. The second sentence starting with “Experimental methods in structural biology…” would be a better choice to give the reader a better idea of what you are actually addressing in this paragraph. The first sentence can still be used later on in the paragraph to motivate the experiments.
- p.1. l.37: I would be reluctant to use the sentence “These approaches can estimate the uncertainty of their answers and provide theoretical guarantees of correctness, …” as there is little underlying theory that even guarantees that the iterates converge (the loss might converge at best, for which there is some theory in the case of RELION)
- In section 2, the authors mainly focus on ModelAngelo. I would recommend to discuss the broader problem so that the reader gets a better feeling for the broader picture
- p.2 l.90: In the second bullet of the contributions the authors claim to compare to sampling methods. In the experiment only one method is discussed. Please change this to singular (method)
- Section 4.3: It feels a bit odd that there is a whole section for the model building part from Cryo-EM maps, but that the other inverse problems are defined in the experiments. I would suggest to create a new section in between what is now section 4 and 5 and discuss all three inverse problems there. This will be useful and more straightforward for the reader who is interested in just one of the applications.
- p.7 l.360: I understand that in equation 13 several terms that are being conditioned on can be removed (\bar{x} in the last term), but for the reader this might be a big step. I would suggest to write out the steps explicitly to get from the left hand side to the right hand side
- p.8 l.409. typo: evalute -> evaluate
- p.9 l.458. What do you mean with the sentence “Note that we do not chose a structure that was resolved with cryo-EM because most cryo-EM-resolved models are incomplete.”
    - Also typo: chose -> choose

### Soundness
3

### Presentation
2

### Contribution
3
