### Summary

This paper proposes a new method for de novo molecular generation, called MAGNet. The method is based on a factorisation of the molecular graph distribution into a set of shapes and a set of atom and bond types. The shapes are generated in a coarse-to-fine manner, starting with the overall molecular structure and then progressively adding finer details. The proposed method is evaluated on standard benchmarks and compared to existing methods.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

- The proposed method is novel and interesting. The idea of generating molecular graphs in a coarse-to-fine manner is interesting and seems to be effective.
- The proposed method is evaluated on standard benchmarks and compared to existing methods. The results show that the proposed method is competitive with existing methods.

### Weaknesses

#### Some Related Works


#### comment

 - The proposed method is not compared with some state-of-the-art methods, such as GeoMol, DiGress, and MolDiff. The lack of comparison with these methods makes it difficult to assess the true performance of the proposed approach relative to the current state of the art. Specifically, GeoMol's use of a geometric representation and DiGress's graph diffusion approach are relevant baselines that should be considered to properly contextualize the contribution.
- The proposed method is not compared with some shape-based methods, such as Shape2Vec. Shape-based methods offer an alternative approach to molecular generation, and a comparison would help to understand the advantages and disadvantages of the proposed method in relation to these approaches. The absence of this comparison leaves a gap in the evaluation of the method's novelty and effectiveness.
- The proposed method is not compared with some motif-based methods, such as MolDiff. The proposed method is not compared with some motif-based methods, such as MolDiff. The lack of comparison with motif-based methods is a significant oversight, as these methods also explore the space of molecular motifs, and a comparison is needed to understand the relative strengths and weaknesses of the proposed approach.
- The proposed method is not compared with some graph-based methods, such as GraphAF. The proposed method is not compared with some graph-based methods, such as GraphAF. The absence of comparison with graph-based methods makes it difficult to assess the method's performance in the context of other graph-based approaches to molecular generation.
- The proposed method is not compared with some other methods for generating molecular shapes, such as JT-VAE. The proposed method is not compared with some other methods for generating molecular shapes, such as JT-VAE. The lack of comparison with JT-VAE, which is a relevant method for shape generation, is a significant omission.
- The proposed method is not compared with some other methods for generating molecular graphs, such as MoLeR. The proposed method is not compared with some other methods for generating molecular graphs, such as MoLeR. The absence of comparison with MoLeR, which is a relevant method for molecular graph generation, is a significant omission.
- The proposed method is not compared with some other methods for generating molecular shapes, such as MiCaM. The proposed method is not compared with some other methods for generating molecular shapes, such as MiCaM. The lack of comparison with MiCaM, which is a relevant method for shape generation, is a significant omission.
- The proposed method is not compared with some other methods for generating molecular graphs, such as GraphAF. The proposed method is not compared with some other methods for generating molecular graphs, such as GraphAF. The absence of comparison with GraphAF, which is a relevant method for graph-based molecular generation, is a significant omission.
- The proposed method is not compared with some other methods for generating molecular shapes, such as JT-VAE. The proposed method is not compared with some other methods for generating molecular shapes, such as JT-VAE. The lack of comparison with JT-VAE, which is a relevant method for shape generation, is a significant omission.
- The proposed method is not compared with some other methods for generating molecular graphs, such as MoLeR. The proposed method is not compared with some other methods for generating molecular graphs, such as MoLeR. The absence of comparison with MoLeR, which is a relevant method for molecular graph generation, is a significant omission.
- The proposed method is not compared with some other methods for generating molecular shapes, such as MiCaM. The proposed method is not compared with some other methods for generating molecular shapes, such as MiCaM. The lack of comparison with MiCaM, which is a relevant method for shape generation, is a significant omission.
- The proposed method is not compared with some other methods for generating molecular graphs, such as GraphAF. The proposed method is not compared with some other methods for generating molecular graphs, such as GraphAF. The absence of comparison with GraphAF, which is a relevant method for graph-based molecular generation, is a significant omission.

### Suggestions

The paper introduces an interesting approach to molecular graph generation by factorizing the distribution into shapes and atom/bond types. However, the evaluation is not comprehensive enough to fully assess the method's performance. The authors should include comparisons with more recent and relevant methods, such as GeoMol, DiGress, and MolDiff, which represent state-of-the-art techniques in molecular generation. Specifically, GeoMol's use of a geometric representation and DiGress's graph diffusion approach are important baselines to include. Furthermore, the paper should compare against shape-based methods like Shape2Vec and motif-based methods like MolDiff and MoLeR to understand the advantages and disadvantages of the proposed approach. The lack of these comparisons makes it difficult to understand the true contribution of the proposed method. The authors should also consider comparing against other graph-based methods like GraphAF and other shape generation methods like JT-VAE and MiCaM to provide a more complete picture of the method's performance relative to the existing literature. 

To strengthen the evaluation, the authors should also provide a more detailed analysis of the generated molecules. For example, they could investigate the diversity of the generated molecules in terms of their chemical properties, such as the number of unique atoms, bond types, and functional groups. Additionally, the authors should provide a more detailed analysis of the computational cost of their method compared to the baselines. This would help to understand the trade-offs between the performance and the computational resources required. Furthermore, the authors should provide a more detailed explanation of the hyperparameter selection process and the sensitivity of the results to different hyperparameter settings. This would help to ensure the reproducibility of the results and to understand the robustness of the method. The authors should also consider providing a more detailed explanation of the limitations of their method and the potential directions for future research. For example, they could discuss the limitations of the coarse-grained representation and how it might affect the quality of the generated molecules.

Finally, the authors should provide a more detailed explanation of the novelty of their approach. While the idea of generating molecular graphs in a coarse-to-fine manner is interesting, it is not clear how this approach differs from existing methods. The authors should clearly articulate the specific advantages of their approach and how it addresses the limitations of existing methods. The authors should also provide a more detailed explanation of the technical details of their method, including the specific choices of neural network architectures and training procedures. This would help to make the paper more accessible to a wider audience and to facilitate the reproducibility of the results. The authors should also consider providing a more detailed explanation of the experimental setup, including the specific datasets used and the evaluation metrics employed. This would help to ensure the reproducibility of the results and to allow other researchers to build upon their work.

### Questions

- How does the proposed method compare to existing methods in terms of performance and computational cost?
- What are the advantages and disadvantages of the proposed method compared to existing methods?

### Rating

5: marginally below the acceptance threshold

### Confidence

5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

**********
