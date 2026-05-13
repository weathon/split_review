# Symbol as Points: Panoptic Symbol Spotting via Point-based Representation

- Decision: Accept
- Scores: 3, 8, 6

## Abstract
This work studies the problem of panoptic symbol spotting, which is to spot and parse both countable object instances (windows, doors, tables, etc.) and uncountable stuff (wall, railing, etc.) from computer-aided design (CAD) drawings. %Unlike raster images, CAD drawings are \yty{Scalable} Vector Graphics(SVG) with geometric primitives such as segments, arcs, and circles. 
Existing methods %for spotting graphical symbols in CAD drawings 
typically involve either rasterizing the vector graphics into images and using image-based methods for symbol spotting, or directly building graphs and using graph neural networks for symbol recognition. In this paper, we take a different approach, \yty{which treats} graphic primitives as a set of \yty{2D} points that \yty{are locally connected} 
and use point cloud segmentation methods to tackle it. Specifically, we utilize a point transformer to extract the primitive features and append a mask2former-like spotting head to predict the final output. \yty{To better use the local connection information of primitives and enhance their discriminability, we further propose the attention with connection module (ACM) and contrastive connection learning scheme (CCL). % to utilize the local interactions among graphical primitives. 
Finally, we propose a KNN interpolation mechanism for the mask attention module of the spotting head to better handle primitive mask downsampling, which is primitive-level in contrast to pixel-level for the image.} Our approach, \yty{named SymPoint, is simple yet effective, outperforming recent} %, is straightforward, faster, and more accurate than existing methods, and outperforms previous 
state-of-the-art method \yty{GAT-CADNet by an absolute increase of 9.6\% PQ and 10.4\% RQ} on the FloorPlanCAD dataset.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In this paper, a method for symbol spotting from CAD vector graphics (VG), called SymPoint, is proposed. SymPoint treats graphic primitives as a set of 2D points. Two strategies, attention with connection module (ACM) and contrastive connection learning (CCL), are devised to better utilize the local connection information of primitives and enhance their discriminability.

### Strengths
The main idea and technical detailed are clearly presented.

### Weaknesses
1. The originality and technical contribution of this work is quite limited. Point Transformer, Mask2Former and InfoNCE are all well-established methods or models.
2. The potential application range of the proposed method can be narrow (CAD vector graphics), because it is unclear whether the idea and techniques presented in this work can be extend ed to other tasks.

### Questions
The authors should explain and verify the originality and technical contribution of the proposed method.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper, titled SymPoint, advocates for representing a symbol as a point and extends the previous methodology to encompass a broader range of symbol properties. The Point Transformer serves as the foundational feature extraction tool. Mask attention and a contrastive connectivity learning mechanism are integrated into the panoptic symbol spotting task, aiming to cultivate rich features that can effectively differentiate between graphic primitives. The PQ performance has been elevated from the previous method to a novel tier, as delineated in the experimental section.

### Strengths
With the advancements in point cloud processing and the Transformer architecture, the authors suggest leveraging these powerful backbones from other domains and adapting them to address the challenge of panoptic symbol spotting.
A suite of techniques, encompassing vector graphics representations, Point Transformers, Masked Attention, Contrastive Connection Learning, and KNN Interpolation, has been integrated into the targeted task.
Experimental outcomes reveal that SymPoint significantly outperforms existing methods, exhibiting a considerable advantage in Semantic Symbol Spotting, Instance Symbol Spotting, and Panoptic Symbol Spotting.

### Weaknesses
- A primary concern from the reviewer centers on the paper's predominant reliance on existing methodologies to address the issue. Specifically, in Sec3.1 (From Symbol to Point), many parameterizations echo those found in FloorplanCAD, albeit this paper seeks to enhance the diversity of encoded features. The point-based representation in Sec 3.2 directly employs the Point Transformer, reminiscent of CADTransformer. Both Contrastive Connection Learning (Sec3.4) and KNN Interpolation (Sec3.5) have been thoroughly examined in other scholarly works. While the "Attention with Connection Module" presents as novel to the reviewer, it would be beneficial to undertake a comprehensive review to discern if analogous concepts have been previous literature.
- In Table 4, where the benchmark approach registers a PQ of 73.1, could you detail the design of how this baseline method is formulated? It is unclear if this baseline is a direct reimplementation of a prior method, or a simplified version of the proposed approach, and this distinction is critical for understanding the significance of the reported improvements.
- In Table 4, it appears the newly introduced "ACM" module inadvertently undermines performance. Could the authors shed light on the causative factors behind this decline? It's important to understand if this is due to a flaw in the module's design, or if it is a result of specific dataset characteristics that the module is not well-suited for. A more detailed analysis of the module's behavior, perhaps with visualizations of the attention maps, would be beneficial.
- Again, referencing Table 4, the KInter technique emerges as a salient contributor to performance enhancement. Could the authors offer a more clear explanation and visualization? It might also be worthwhile to highlight this module within the methods section. The current description lacks sufficient detail to understand why KNN interpolation is superior to other interpolation methods, and how it is specifically implemented within the framework. A visual comparison of the interpolation results would be very helpful.
- As the proposed framework incorporate a bunch of techniques for a specific application, did you submit the code for reviewing?

### Questions
See the raised concens in Weaknesses section

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes a new method for symbol segmentation in architectural floorplans. The method is based on representing each graphical primitive as a point with a set of features and thus, relying on Point Transformer for feature extraction. Then, an adaptation of Mask2Former is used to segment and classify the symbols in the floorplan. Some specific components are introduced to adress the specificity of graphical primitives in architectural drawings. Experimental validation is performed by applying the method to a standard floorplan dataset, comparing with state-of-the-art and conducting several ablation studies.

### Strengths
- The idea of relying on a point representation of graphical primitives seems novel and makes sense in this context since symbols in architectural drawings are composed of graphical primitives. Then, using the combination of PointTransformer and Mask2Former is also a novel approach in this context that seems suitable for capturing the interaction between graphical primitives for symbol segmentation. 
- Experimental results on a standard dataset report better performance than state-of-the-art methods. A detailed ablation study shows the contribution of the different modules of the proposed framework.

### Weaknesses
Perhaps I missunderstood something, but I do not see the motivation of symbol segmentation in CAD drawings. As far as I understand CAD drawings should already contain information about the symbols included in the floorplan and where they are located.

In the description of the method and the experiments there are several points that are confusing or not well explained:
- In equation (2) I understand that l_k is the distance between v_1 and v_2. Then, what about circles and ellipses? How is the lengh computed? And for arcs, this definition does not account for the curvature. Two arcs with very different curvature can have the same representation.
- In equation (3), it is not clear how the neighbourhood M(p_i) is defined. Do adjacent points mean connected primitives? Or primitives inside a certain distance? Which is exactly the difference with A(p_i) defined later in section 3.3 (given that the threshold used in section 3.3 is just one pixel). In this sense, the role of the ACM module is not very clear. 
- It is not clear the motivation of the KNN interpolation described in section 3.5. As far as I understand, since points correspond to graphical primitives, interpolation of neighboring points could lead to losing information of specific primitives and I am not sure that makes sense merging different primitives into a new one. 
- Related to the previous point, It is not clear how it is performed downsamplind and upsampling in the Point Transformer. The same as in the original Point Transformer? 
- In equation (12) it is not clear what is e_i and L(e_i).
- In the experiments, which is the difference between Semantic and Panoptic Symbol Segmentation? Why in table 1 (semantic segmentation) the evaluation measure is F1? How are F1 and wF1 defined in this context?

### Questions
See above in Weaknesses

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
