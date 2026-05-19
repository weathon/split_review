### Summary

This paper proposes a single-view 3D reconstruction method based on triplane-NeRF. The authors use a large transformer-based encoder-decoder architecture to learn a triplane representation from a single image. The triplane representation is then used to render novel views of the object using a NeRF decoder. The method is trained on a large-scale dataset of 3D objects and videos, and is able to reconstruct high-quality 3D shapes from a single image in just 5 seconds. The authors also demonstrate the effectiveness of their method on a variety of real-world and generated images.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper introduces a novel approach to single-view 3D reconstruction using a large transformer-based encoder-decoder architecture. The method is able to learn a triplane representation from a single image, which is then used to render novel views of the object using a NeRF decoder.

2. The method is trained on a large-scale dataset of 3D objects and videos, and is able to reconstruct high-quality 3D shapes from a single image in just 5 seconds.

3. The authors demonstrate the effectiveness of their method on a variety of real-world and generated images, and show that it outperforms existing methods in terms of both quality and speed.

### Weaknesses

#### Some Related Works


#### comment

1. The method assumes that the input images are of objects without backgrounds, and does not handle the background. This is a significant limitation as many real-world images contain complex backgrounds that can interfere with the reconstruction process. The method's reliance on background-free inputs restricts its applicability in practical scenarios where such ideal conditions are rarely met. For instance, images captured in cluttered environments or with overlapping objects would pose a challenge for the proposed approach.

2. The method assumes Lambertian objects and does not model view-dependent effects such as specular reflections. This assumption limits the method's ability to accurately reconstruct objects with non-Lambertian surfaces, which are common in real-world scenarios. The lack of view-dependent modeling means that the method will likely fail to capture the nuances of specular highlights and other complex lighting effects, resulting in less realistic reconstructions. For example, objects with glossy or metallic surfaces would not be accurately represented.

### Suggestions

The authors should explore methods to incorporate background handling into their pipeline. One approach could be to use segmentation techniques to isolate the object of interest from the background before feeding it into the reconstruction network. This would allow the method to be applied to a wider range of real-world images. Alternatively, the authors could investigate techniques for learning background representations alongside the object representation, which could potentially improve the robustness of the method to background clutter. This could involve using a separate branch in the network to process background information or incorporating attention mechanisms to focus on the foreground object. Furthermore, the authors could consider using datasets with more complex backgrounds during training to improve the model's ability to generalize to such scenarios.

To address the limitation of assuming Lambertian objects, the authors should investigate incorporating view-dependent effects into their NeRF decoder. This could involve using a more sophisticated rendering equation that accounts for specular reflections and other non-Lambertian effects. One approach could be to use a BRDF (Bidirectional Reflectance Distribution Function) to model the surface reflection properties, which would allow the method to capture the nuances of specular highlights and other complex lighting effects. Another approach could be to use a neural network to learn the view-dependent appearance of the object, which could potentially improve the realism of the reconstructions. The authors could also consider using datasets with more complex lighting conditions during training to improve the model's ability to generalize to such scenarios.

Finally, while the authors mention the use of a large-scale dataset, it would be beneficial to provide more details about the dataset's composition and diversity. Specifically, it would be helpful to know the types of objects included in the dataset, the range of viewpoints and lighting conditions, and the presence of any background clutter. This information would allow readers to better assess the generalizability of the proposed method and identify potential limitations. Furthermore, the authors should consider releasing the dataset to the research community to facilitate further research in this area.

### Questions

1. How does the method handle images with complex backgrounds or occlusions?

2. How does the method perform on objects with non-Lambertian surfaces or view-dependent effects?

### Rating

6: marginally above the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
