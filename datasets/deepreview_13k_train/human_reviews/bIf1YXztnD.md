# Orient Anything

- Decision: Reject
- Scores: 6, 5, 5

## Abstract
Orientation estimation is a fundamental task in 3D shape analysis which consists of estimating a shape's orientation axes: its side-, up-, and front-axes. Using this data, one can rotate a shape into canonical orientation, where its orientation axes are aligned with the coordinate axes. Developing an orientation algorithm that reliably estimates complete orientations of general shapes remains an open problem. We introduce a two-stage orientation pipeline that achieves state of the art performance on up-axis estimation and further demonstrate its efficacy on full-orientation estimation, where one seeks all three orientation axes. Unlike previous work, we train and evaluate our method on all of Shapenet rather than a subset of classes. We motivate our engineering contributions by theory describing fundamental obstacles to orientation estimation for rotationally-symmetric shapes, and show how our method avoids these obstacles.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes a supervised method for predicting the orientation of a 3D object. The main observation is that direct regression will fail due to the abundance of symmetry in 3D shapes. Therefore, a two-stage approach is approached. Using the DGCNN backbone, the method first regresses the orientation up to octahedral symmetries (chosen as it is the single group that contains the most common symmetries in SO3). Then, the method classifies the transfomation that "flips" the shape, oriented by the first step, into the correct orientation. The method is intuitively sound and avoids issues with previous regression based works, by having better overall performance, work on more general settings (full orientation, single model over entire collection of shapes, instead of per catregory), and have error characteristics (centered around few modes) that make further human-in-the-loop correction easier.

### Strengths
- Practically useful approach that clearly contributes to an important problem in 3D shape analysis. Clearly outperforms relevant works, achieving better quantitative performance and is more general.
- The idea/intuition behind this approach is not only useful for the particular setting (orientation estimation), but generally applicable to a much wider range of 3D tasks where certain steps involve predictions that can be complicated by symmetries (just naming a few that comes to my mind: part-based analyis/generation, assembly, articulation, shape retrieval, etc.)
- Solid mathematical analysis to back up the method - though I do not have the background to and did not check thoroughly for its correctness. The proofs does sound reasonable.

### Weaknesses
 - One could argue that the method itself, though wrapped in solid mathematics, is not *that* novel, since hybrid classification+regression strategies are very common overall, and the key observations about symmetries complicating L2 regression is not new. It might help to further discuss/clarify the novelty.
- The octahedral group, while covering a good amount of 3D symmetries, also leave out a lot of important ones e.g. the very common 5-way symmetry for chair bases, many mechnical objects e.g. bolts/gears. While I think there can be extensions to this method to cover an even wider range of shapes, the present version probably would not work well on these. And unlike a single step approach, I do have the feeling that this method will struggle a lot more for these shapes. Some analysis here would be ideal - either on how to sidestep these cases or to show that the proposed method works no worse than single step approaches.
- Arguably, ShapeNet is no longer the go-to dataset now given that there exist much larger shape datasets now. Would be interesting to see more analysis there. Figure 11 does cover objaverse but might be good to have more in the main body.

### Questions
I am overall leaning towards acceptance. I think this paper contains a solid, although somewhat straightforward, idea, that can be useful in many applications. I am currently not willing to champion for the paper, as I am personally not too sure about the magnitude of impact this paper can make, and given that there are clearly cases where the proposed method cannot solve (but perhaps can be adapted to solve). More clarification on novely/contribution and more analysis on these potential limitations can make me more positive.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper presents an approach to predict the canonical 3D pose of an arbitrarily posed 3D point cloud of an object. The proposed two-stage pipeline first predicts an upright pose, using a DGCNN backbone to regress a rotation matrix from a point cloud. Then it performs a 24-way classification to resolve the remaining degree of freedom. Compared to Upright-Net (2022), it is able to find the upward orientation better on ShapeNet and ModelNet40. Top-1 and top-4 accuracy is reported for full orientation prediction.

### Strengths
Clarity: easy to read and the problem definition is clear.

### Weaknesses
In my view, the technical rigor does not meet the conference's standards. I appreciated the careful explanation and presentation, but spending multiple pages on why a direct L2 regression of rotational symmetry doesn't work seems unnecessary. Considering the presentation and focus of other papers published in this venue, I think this could be seen as common sense. I did not find enough significance, although it may be that no one's done this exact proof before.

Experimental validation: Upright-Net is the only other method compared against. While the numbers are better, I think the experiments are simple enough that a more thorough validation should have been done; using the same backbone network, etc. And I was not sure what the take-home message was; so is it better to predict the upright pose as a matrix and orthogonalize as presented? What was the reason for the improvement? And for the full-orientation prediction, N-way classification is a reasonable approach, but it is not compared against any baseline, and the final pose is dependent on the upright direction prediction which I did not find convincing enough.

### Questions
Experiment suggestion: The paper says "our method reliably provides a plausible set of candidate orientations for diverse shapes unseen during training". I think it might be good to do a novel category evaluation experiment.

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
4

### Summary
The paper addresses the problem of estimating the orientation of rigid 3D shapes. The paper starts from the fact that, theoretically, it is not possible to have a function that, for any arbitrarily oriented shape with non-trivial rotational symmetries, predicts the right orientation (output is not unique, so such a map cannot be a function). The paper also shows that L2 objectives are not suitable for recovering the solution by optimization.

Hence, the paper proposes to decompose the problem in two parts:
1) The Quotient Orienter: a neural network (DGCNN) that solves for the rotation with an L2 objective quotient by the octahedral group.
2) The Flipper: a neural network (DGCNN) trained to solve a classification problem to recover one of the 24 octahedral flips, returning the canonical orientation.

The approach is compared against one baseline, which shows significantly better accuracy on ShapeNet and ModelNet.

### Strengths
- The paper addresses a valuable problem that could potentially impact many different research areas. Symmetries have been widely studied in computer graphics and computer vision and have mainly focused on the recent Geometric Deep Learning theory. 
- While previous approaches focus on learning orientation for a single object class, the proposed approach aims to provide a unified model that works on all the object classes at once.
- The theoretical discussion of the paper seems reasonable, and the code is provided in supplementary. This could be an instrumental tool for several downstream tasks, and results are probably easy to replicate.

### Weaknesses
1) My main concern lies in the experimental evaluation of the approach. The method compares against Upright-net, Shapenet, and ModelNet. Although I consider favorably the use of the entire ShapeNet dataset, I generally think more comparisons would be informative. For example, ART ("Adjoint Rigid Transform Network: Task-conditioned Alignment of 3D Shapes", Zhou et al., 3DV 2022) seems relevant but not discussed in the paper and could serve as a baseline for the category of "canonical alignment" methods. Notice that ART also showcases results on humans. This latter is also an interesting domain, and I would be interested to know the authors' opinions on whether their method would suit this case. Similarly, I evaluate positively that the method has been tested on Objaverse, but the few qualitative examples do not help to understand the actual flexibility of the method.
2) Although I enjoyed reading the method, I think there is room to improve the presentation. The most severe problem is probably the choice of qualitative visualization, which is difficult to read and compare. I would suggest visualizing fewer examples but bigger ones with clearer axe orientations, as well as pairing them with the GT for comparison. The method is also quite extensive. In the end, the conclusion is relatively straightforward: although the problem of recovering an orientation cannot be formulated as a function, it is actually enough to restrict to predict one valid solution (and actually, the only doable things, since the solution in the same equivalence class are indistinguishable). As a consequence, this also makes the problem tractable with an L2 optimization. This is reasonable and could be expressed in a much more direct way. Finally, Figure 6 seems a bit deceptive due to the logarithmic scale. The number of valid shapes (bars on the left of the dashed lines) seems similar between the two methods, but the quantitative metrics indicate differently. The larger difference between the blue and red bars is often in the scale of 10¹, while some small differences in the bins of 90 and 180 degrees are actually in the 10³. I suggest removing the logarithmic scale or providing a cumulative curve visualization (e.g., on the y-axis, the percentage of shapes below or equal to the x-axis angular error).
3) The papers do not offer any ablation nor analysis of the method. This would be important to validate intuition and guide future work. For example:
(a) how would the Flipper perform without the quotient oriented or with an oriental that does not quotient the space? 
(b) How does the model scale with the number of different data and classes? Is it beneficial to consider all the classes together, or would it be better to train specialized models for every class? 
(c) What is the computational time in terms of inference and training? 
(d) Figure 6 seems to suggest that the error of the proposed method focuses on some sharp bins (e.g., 90 and 180 degrees, but also 45 and 135 for ModelNet). Is it due to the octahedral nature of the Flipper classifier? 
(e) Why use octahedral and not icosahedral symmetries? 

I think these are all aspects that would be worth further investigation.

### Questions
Please, refer to the questions listed in points (1) and (3) of weaknesses.

Minor:
1) Line 335:"We observe that our quotient orienter [...] fails for a small subset of rotations". Could you elaborate more on this? Have you noticed a recurrent pattern in the failure mode?
2) "Our method improves on Upright-Net’s up-axis estimation accuracy by nearly 20 percentage points, corresponding to a 64.6% reduction in the error rate relative to the previous state of the art.". Could you elaborate a bit more about what are the terms of this "reduction"?

### Soundness
3

### Presentation
2

### Contribution
2
