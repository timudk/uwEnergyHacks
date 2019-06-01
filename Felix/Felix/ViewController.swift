//
//  ViewController.swift
//  Felix
//
//  Created by James Dorfman on 2019-06-01.
//  Copyright © 2019 James Dorfman. All rights reserved.
//

import UIKit


class ViewController: UIViewController {

    @IBOutlet weak var circularImage: UIImageView!

    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view.
        
        circularImage.layer.masksToBounds = true
        circularImage.layer.cornerRadius = circularImage.bounds.width / 2
    }

}

