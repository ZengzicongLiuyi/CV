import cv2
import numpy as np

def preprocess_images(left_path, right_path, target_size=(800, 600)):
    """
    预处理图像:读取、调整大小、确保尺寸合适
    """
    # 读取图像
    left_img = cv2.imread(left_path)
    right_img = cv2.imread(right_path)
    
    if left_img is None or right_img is None:
        raise ValueError("无法读取图像文件")
    
    # 调整图像尺寸为2的倍数
    target_w = target_size[0] - (target_size[0] % 2)
    target_h = target_size[1] - (target_size[1] % 2)
    
    # 调整两张图片到相同的目标尺寸
    left_img = cv2.resize(left_img, (target_w, target_h))
    right_img = cv2.resize(right_img, (target_w, target_h))
    
    # 转换为float32类型
    left_img = left_img.astype(np.float32)
    right_img = right_img.astype(np.float32)
    
    # 创建三通道掩码，与图像维度匹配
    mask = np.zeros((target_h, target_w, 3), dtype=np.uint8)
    mask[:, :target_w//2] = 255
    
    return left_img, right_img, mask

class LaplacianBlending:
    def __init__(self, left, right, mask, levels=4):
        self.left_img = left
        self.right_img = right
        self.mask = mask
        self.levels = levels
        self.build_pyramids()

    def build_pyramids(self):
        self.left_lap_pyr, self.left_highest_level = self.build_laplacian_pyramid(self.left_img)
        self.right_lap_pyr, self.right_highest_level = self.build_laplacian_pyramid(self.right_img)
        self.mask_gau_pyr = self.build_gaussian_pyramid(self.mask)

    def build_laplacian_pyramid(self, img):
        lap_pyr = []
        current_img = img.copy()
        for _ in range(self.levels):
            down = cv2.pyrDown(current_img)
            up = cv2.pyrUp(down, dstsize=(current_img.shape[1], current_img.shape[0]))
            lap = cv2.subtract(current_img, up)
            lap_pyr.append(lap)
            current_img = down
        return lap_pyr, current_img

    def build_gaussian_pyramid(self, img):
        gau_pyr = [img.copy()]
        current_img = img.copy()
        for _ in range(self.levels):
            down = cv2.pyrDown(current_img)
            gau_pyr.append(down)
            current_img = down
        return gau_pyr

    def blend(self):
        blend_highest = self.left_highest_level * (self.mask_gau_pyr[-1] / 255.0) + \
                       self.right_highest_level * (1.0 - self.mask_gau_pyr[-1] / 255.0)
        
        blend_lap_pyr = []
        for i in range(self.levels):
            blend_lap = self.left_lap_pyr[i] * (self.mask_gau_pyr[i] / 255.0) + \
                       self.right_lap_pyr[i] * (1.0 - self.mask_gau_pyr[i] / 255.0)
            blend_lap_pyr.append(blend_lap)

        blend_img = blend_highest
        for i in range(self.levels-1, -1, -1):
            blend_img = cv2.pyrUp(blend_img, dstsize=(blend_lap_pyr[i].shape[1], blend_lap_pyr[i].shape[0]))
            blend_img = cv2.add(blend_img, blend_lap_pyr[i])

        return blend_img

def laplacian_blend(left, right, mask):
    laplace_blend = LaplacianBlending(left, right, mask, 4)
    return laplace_blend.blend()

if __name__ == "__main__":
    try:
        # 预处理图像
        left_img, right_img, mask = preprocess_images(
            "R-C.jpg", 
            "OIP-C (4).jpg",
            target_size=(500, 600)  # 可以根据需要调整目标尺寸
        )
        
        # 执行融合
        blend_img = laplacian_blend(left_img, right_img, mask)
        
        # 保存结果
        cv2.imwrite("result.jpg", blend_img)
        print("图像融合完成，结果已保存为 result.jpg")
        
    except Exception as e:
        print(f"发生错误: {str(e)}")

        