# HPU Web Interface

This is the code for hosting HPU Interface locally on your computer. One can install any of the popular apache web development environment. I used xampp which can be found [here]. The description of the four exteriments are as follows:

* HPU1: Draw the bounding boxes without any prior CPU algorithm.
* HPU2: Given a CPU algorithm, Click on all detected bounding boxes that do not contain pedestrians.
* HPU3: Given a CPU prediction, Locate and draw bounding boxes around pedestrians that have NOT been detected.
* HPU4: Given a CPU algorithm, click on objects not enclosed by bounding box. Then, the CPU chooses the bounding box from the predicted boxes below the threshold to place round it 

### How to run the Interface:
* Save the folder contents in your localhost folder (usually at /var/www/html )
* Initialize all .count files to '1' and clear all .data files in the /data/log folder
* Go to the folder and enter the following command to start the server
```sh
$ sudo python flask_app.py
```
* Now open the chrome browser and go to http://127.0.0.1:5000/hpu1 to start the hpu1 interface. This can very well be modified to run hpu2, hpu3 and hpu4

### How to record the data:

The data gets recorded in the /data/log folder in the corresponding .dat files. The format of data recorded in a space separated format is as follows:
* hpu1.data: [image_id] [no. of boxes] [time in seconds] [x-coord, y-coord, width, height]  
Example: 12 2 10.36 82.85 57.12 100 300 266.05 48.04 100 300  
* hpu1.data: [image_id] [no. of boxes] [time in seconds] [0 if the box is false positive, 1 otherwise]        
Example: 10 3 2.848 1 0 0
* hpu3.data: [image_id] [no. of new boxes] [time in seconds] [x-coord, y-coord, width, height]                  
Example: 12 1 5.19 119.99 36.42 150 300
* hpu4.data: [image_id] [no. of new boxes] [time in seconds] [x-coord, y-coord]                   
Example: 14 1 4.59 389.69 181.75

### How to modify the code for your own purposes:

The areas of the code you need to modify are as follows:
* /static/images folder: Add your images here in the form test-[image_id].png. Other image formats are also supported, you need to change line 27 of flask_app.py accordingly. 
* /data/confident folder: Add the bounding boxes for each image in the corresponding file of the form test-[image_id].dat. The file contents should be space separated and of the form [x-coord] [y-coord] [height] [width]. Every box should be in a new line. 

That's it! You are ready to go..! Run the interface, record your data and plot the graphs. 

NOTE 1: This interface is designed for pedestrian dataset. Hence, those working on other datasets may need to modify the click_handler(), x_handler() and z_handler() functions in hpu1.js, hpu3.js and hpu4.js. This is because the default box created on clicking the image will have different aspect ratio for different dataset. Here is an example for car dataset: 



  function click_handler(cx, cy) {
      ...
      if(!new_box && current_box == -1) {
    new_box = true;

    x = cx / image.scale - 50;
    y = cy / image.scale - 20;
    w = 100;
    h = 40;

    image.temp_box = new Box(-2, x, y, w, h, image);
    image.active_box = -2;
    ...
  }
  
  function x_handler() {
    ...
      var cx = image.boxes[index].x + 0.5 * image.boxes[index].w;
      var cy = image.boxes[index].y + 0.5 * image.boxes[index].h;

      if(image.boxes[index].w < 135) {

        image.boxes[index].w += 1.25 * image.scale;
        image.boxes[index].h += 0.5 * image.scale;

        image.boxes[index].x = cx - 0.5 * image.boxes[index].w;
        image.boxes[index].y = cy - 0.5 * image.boxes[index].h;
    ...
  }

NOTE 2: The 'Postman' extention in chrome is helpful in debugging the GET requests. 

[here]: https://www.apachefriends.org/download.html
  







