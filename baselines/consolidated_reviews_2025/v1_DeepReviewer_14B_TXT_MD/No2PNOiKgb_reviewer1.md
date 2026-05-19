### Summary

The paper proposes two main improvements over the prior work (Vavilala_2023_ICCV) for fitting a set of convex primitives to the scene. First, it allows a small number of negative primitives in the sense of CSG. Second, it shows that an appropriately constructed ensembling method produces very strong improvements in accuracy.

### Soundness

2

### Presentation

1

### Contribution

2

### Strengths

The paper proposes two main improvements over the prior work (Vavilala_2023_ICCV) for fitting a set of convex primitives to the scene. First, it allows a small number of negative primitives in the sense of CSG. Second, it shows that an appropriately constructed ensembling method produces very strong improvements in accuracy.

### Weaknesses

#### Some Related Works


#### comment

 - The paper is not very well written and hard to follow. It is not clear how exactly the ensemble is created and how the negative primitives are used during fitting.
- The authors claim that they use vertical and horizontal flips but it is not clear if they also use random rotations as in the prior work.
- The authors claim that their approach outperforms CAPRI-Net (Yu et al., 2022) but it is not clear how is the comparison done since CAPRI-Net uses a different set of primitives. The authors should compare the performance with CAPRI-Net directly using the same metrics and evaluation protocol to validate their claim. The current comparison is not valid due to the different primitive sets and evaluation methodologies.

### Suggestions

The paper needs significant clarification regarding the ensemble creation and the role of negative primitives. The description of the ensemble construction is vague, making it difficult to understand how the different models are trained and combined. Specifically, it is unclear what parameters are varied to create the ensemble and how the ensemble prediction is obtained. The authors should provide a detailed algorithm or pseudocode that clearly outlines the ensemble creation process. Furthermore, the explanation of how negative primitives are incorporated into the fitting process is insufficient. It is not clear how the Boolean operations are performed, and how the negative primitives influence the overall shape representation. A more detailed explanation, possibly with illustrative examples, is needed to clarify this aspect.

Regarding the data augmentation, the authors should explicitly state whether random rotations are used in addition to vertical and horizontal flips. If random rotations are not used, a justification for this decision should be provided, especially since the prior work on primitive fitting often employs such augmentations. The absence of random rotations might limit the generalization capability of the model, and this should be addressed. Furthermore, the authors should clarify how the camera calibration parameters are used to adjust the point cloud during the flip augmentations. A detailed explanation of this process is crucial for the reproducibility of the results. The authors should also discuss the impact of these augmentations on the performance of the model.

Finally, the comparison with CAPRI-Net is not valid in its current form. The authors should either compare with CAPRI-Net using the same metrics and evaluation protocol or clearly state that the comparison is not directly comparable due to the different primitive sets and evaluation methodologies. If a direct comparison is not possible, the authors should acknowledge the limitations of the comparison and avoid making strong claims about outperforming CAPRI-Net. Instead, they should focus on the strengths of their approach and its contributions to the specific problem of convex primitive fitting. The authors should also consider comparing their method with other relevant baselines in the field of primitive fitting, using consistent evaluation metrics.

### Questions

- The authors claim that they use vertical and horizontal flips but it is not clear if they also use random rotations as in the prior work.
- The authors claim that their approach outperforms CAPRI-Net (Yu et al., 2022) but it is not clear how is the comparison done since CAPRI-Net uses a different set of primitives. The authors should compare the performance with CAPRI-Net directly using the same metrics and evaluation protocol to validate their claim.

### Rating

3

### Confidence

4

**********
