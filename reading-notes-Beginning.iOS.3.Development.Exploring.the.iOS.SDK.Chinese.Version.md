Reading Notes:Beginning iOS 3 Development Exploring the iOS SDK(Chinese Version)
==========
## Chapter 1 and 2 Welcome##
* The first app:[hello, iOS!](http://github.com/codepongo/utocode/ios/)
* Xcode
 + groups & Files
* Interface Builder
 + xib window
  - File's Owner
  - add a object and connect it to source code object
 + view window
 + library window
 + inspector
  - attributes
  - connection
  - size
  - identify
* icon
 $\_Info.plist -> Icon File

## Chapter 3 Handling Basic Intraction##
### Xcode project templates ###
### MVC pattern ###
### IBOutlet ###
<pre data-language="objc">
@property (nonatomic, retain) IBOutlet Class * object;
</pre>
<pre data-language="objc">
@synthesize object;
</pre>
### IBAction ###
<pre data-language="objc">
- (IBAction) functionName:(id)sender;
</pre>
<pre data-language="objc">
- (IBAction) funtionName:(id) sender {
}
</pre>
### UIApplicationDelegate ###
### ViewController ###

## Chapter 4 More User Interface Fun##
### UIImageView ###
### UILabel ###
### UITextField ###
+ Return or Done
 - Return:change the another view
 - Done:back to the current view
+ Closing the keyboard
 - UITextField,  Did End On Exit
 - UIControl, Touch Down 
 - resignFirstResponder
### UISlider ###
* Value Changed


### UISwitch ###
### UISegmentedControl ###
* Value Changed


### UIButton ###
* Touch Up Inside


### comment ###
* //TODO:


### Action Sheet ###
#### implement action sheet ####
<pre data-language="objc">
UIActionSheet a = [[UIActionSheet alloc] initWithTitle:@"title" delegate:self cancelButtonTitle:@"Cancel" destructiveButtonTitle:@"OK" otherButtontitle:nil];
[a showInView:self.view];
[a release];
</pre>
#### UIActionSheetDelegate, didDismissWithButtonIndex ####


### Alert ###
#### implement alert ####
<pre data-language="objc">
UIAlertView a = [[UIAlertView alloc] initWithTitle:@"t" message:@"m" delegate:nil cancelButtonTitle:@"Cancel" otherButtonTitles:nil];
</pre>
#### UIAlertViewDelegate ####


## Chapter 5 rotation and resize ##
### iPhone4(iPhone3, iPhone3 GS) pixel: 320x480 ###
<pre data-language="objc">
- (BOOL) shouldAutorotateToInterfaceOrientation:(UIInterfaceOrientation) interfaceOrientation;
- (BOOL) willAnimateRotationToInterfaceOrientation:(UIInterfaceOrientation) interfaceOrientatio duration:(NSTimeInterval) duration;
</pre>
<pre data-language="objc">
//UIInterfaceOrientationProtrait
//UIInterfaceOrientationProtraitUpsideDown
//UIInterfaceOrientationLandcapeLeft
//UIInterfaceOrientationLandcapeRight
if (interfaceOrientation == UIInterfaceOrientationPortrait)
{
	button.frame = CGRectMake(0,0,100,100);
}
</pre>
### portrait and landscape views ###
<pre data-language="objc">
self.view = self.portrait;
</pre>

## Chapter 6 Multiview ##
subview size by Interface Builder:Attributes - Simulated User Interface Elements
### switch view ###
<pre data-language="objc">
[self.oldViewController viewWillDisappear:YES];
[self.newViewController viewWillAppear:YES];
[self.oldViewController.view removeFromSuperView];
[self.view insertSubview:self.newViewController.view atIndex:0];
[self.oldViewController viewDidDisappear:YES];
[self.newViewController viewDidAppear:YES];
</pre>
### view animation ###
<pre data-language="objc">
[UIView beginAnimations:@"view flip" context:nil];
[UIView setAnimationDuration:1.25];
[UIView setAnimationCurve:UIViewAnimationCurveEaseInOut];
//UIViewAnimationTransitionFlipFromRight
//UIViewAnimationTransitionFlipFromLeft
//UIViewAnimationTransitionFlipCurlUp
//UIViewAnimationTransitionFlipCurlDown
[UIView setAnimationTransition:UIViewAnimationTransitionFlipFromRight forView:self.view cache:YES];
</pre>
## Chapter 7 Tab bars and Pickers ##
### Tab bars ###
 + View Controllers
 + icon 24x24 pixel
 + Tab Bar Item


### Picker ###


#### Date Picker ####
<pre data-language="objc">
//set
NSDate * now = [[NSDate alloc] init];
[datePicker setDate: now animated:NO];
[now release];
//get
NSDate d = [datePicker date];
</pre>


#### Picker ####
<pre data-language="objc">
#pragma mark -
#pragma mark Picker Data Source Methods
- (NSInteger) numberOfComponentsInPickerView:(UIPickerView * )pickerView {
	return column_number;
}
- (NSInteger)pickerView:(UIPickerView * )pickerView numberOfRowsInComponent:(NSInteger) component {
	return row_count;
}
#pragma mark -
#pragma mark Picker Delegate Methods
- (NSString * )pickerView:(UIPickerView * )pickerView titleForRow:(NSInteger) row forComponent:(NSInteger) component {
	return row_component_string;
}
- (CGFloat)pickerView:(UIPickerView * )pickerView withForComponent:(NSInteger) component {
	return the_width_of_the_component;
}
</pre>
#### Custom Picker ####
<pre data-language="objc">
#pragma mark -
#pragma mark Picker Delegate Methods
- (UIView * )pickerView:(UIPickerView * )pickerView viewForRow:(NSInteger) row forComponent:(NSInteger)component reusingView:(UIView * ) view {
}
</pre>
#### UIPickerView rolls and selects row####
<pre data-language="objc">
[picker selectRow:newValue inComponent:i animated:YES];
[picker reloadComponent:i];
</pre>
### Audio ###
import AudioToolbox.framework - Reference Type:Relative to Current SDK
<pre data-language="objc">
#import <AudoToolbox/AudioServices.h>
NSString * path = [[NSBundle mainBundle]pathForResource:@"crunch" ofType:@"wav"];
SystemSoundID s;
AudioServicesCreateSystemSoundID((CFURLRef)[NSURL fileURLWithPath:path], &s);
AudioServicesPlaySystemSound(s);
</pre>
### delay to perform ###
<pre data-language="objc">
[self performSelector:@selector(function-name) withObject:nil afterDelay:.5];
</pre>
### pragma ###
<pre data-language="objc">
#pragma mark -
#pragma mark Picker Data Source Methods
</pre>
### bundle ###
<pre data-language="objc">
NSBundle * b = [NSBudle mainBundle];
NSString * p = [b pathForResource:@"name", ofType:@"suffix"];
</pre>

## Chapter 8 Table Views##
###  Grouped and Plain tables ###
###  data source and delegate ###
<pre data-language="objc">
#pragma mark -
#pragma mark Table View Data Source Methods
- (NSInteger) tableView:(UITableView * )tableView numberOfRowsInSection:(NSInteger)section {
	return count_of_rows_in_section;
}
- (UITableViewCell * )tableView:(UITableView * )tableView cellForRowAtIndexPath:(NSIndexPath * )indexPath {
	static NSString tableId = @"";
	UITableViewCell * c = [tableView dequeueReusableCellWithIdentifier:tableId];
	if (c == nil) {
		//UITableViewCellStyleSubtitle
		//UITableViewCellStyleValue1
		//UITableViewCellStyleValue2
		c = [[[UITableViewCell alloc]initWithStyle:UITableViewCellStyleDefault reuseIdentifier:tableId] autorelease];
	}
	c.imageView.image = [UIImage imageNamed:@"name.png"];
	c.textLabel.text = [String stringWithFormat:@"%d", [indexPath row]];
	c.detailTextLabel.text = @"detail";
	return c;
}
#pragma mark -
#pragma mark Table View Data Delegate Methods
- (NSInteger) tableView:(UITableView * )table indentationLevelForRowAtIndexPath:(NSIndexPath * )indexPath {
	return indentation_level;
}
- (NSIndexPath * ) tableView:(UITableView * )table willSelectRowAtIndexPath:(NSIndexPath * )indexPath {
	return indexPath;
}
- (void) tableView:(UITableView * )table didSelectRowAtIndexPath:(NSIndexPath * )indexPath {
	[tableView deselectRowAtIndexPath:indexPath animated:YES];
}

- (CGFloat) tableView:(UITableView * )tableView heightForRowAtIndexPath:(NSIndexPath * )indexPath {
	return height;
}
</pre>
### Custom ###
#### child view ####
<pre data-language="objc">
- (UITableViewCell * )tableView:(UITableView * )tableView cellForRowAtIndexPath:(NSIndexPath * )indexPath {
	static NSString tableId = @"";
	UITableViewCell * c = [tableView dequeueReusableCellWithIdentifier:tableId];
	if (c == nil) {
		c = [[[UITableViewCell alloc]initWithStyle:UITableViewCellStyleDefault reuseIdentifier:tableId] autorelease];
	}
	CGRect rc = CGRectMake(0, 16, 70, 15);
	UILabel * l = [[UILabel alloc] initWithFrame:rc];
	[c.contentView addSubview:l];
	return c;
</pre>
#### inherit UITableViewCell ####
<pre data-language="objc">
- (UITableViewCell * )tableView:(UITableView * )tableView cellForRowAtIndexPath:(NSIndexPath * )indexPath {
	static NSString tableId = @"";
	CustomCell * c = (CustomCell * )[tableView dequeueReusableCellWithIdentifier:tableId];
	if (c == nil) {
		NSArray * nib = [[NBundle mainBundle] loadNibNamed:@"CustomCell" owner self options:nil];
		for (id obj in nib) {
			if ([obj isKindOfClass:[CustomCell class]]) {
				c = (CustomCell * )obj;
			}
		}
	}
	return c;
}
</pre>

### Section ###
<pre data-language="objc">
- (NSInteger) numberOfSectionsInTableView:(UITableView * )tableView {
	return count_of_section;
}
- (NSString * )tableView:(UITableView * )table titleForHeaderInSection:(NSInteger)section {
	return [NSString stringWithFormat(@"%@", section)];
}
</pre>
### Indexed ###
<pre data-language="objc">
- (NSArray * )sectionIndexTitlesForTableView:(UITableView * )tableView {
	return ;
}
</pre>
### search ###
* earch bar
 + searchBarTextDidBeginEditing:
 + searchBar:textDidChange
 + searchBarCancelButtonClicked


## Chapter 9 Navigation Controllers and Table Views##
### Navigation ###
#### 1. add nav(UINavigationController) in window(NSWindow)####
<pre data-language="objc">
[window addSubview:nav];
</pre>
#### 2. set firstView(UITableViewController) as nav rootViewController ####
Root View Controller identify is firstCtrller
#### 3. title ####
<pre data-language="objc">
firstCtrller.title = @"title"
</pre>
#### 4. navigate a view ####
<pre data-language="objc">
[nav pushViewController:subController animated:YES];
</pre>
#### 5. back to view ####
<pre data-language="objc">
[nav popViewControllerAnimated:YES];
</pre>

### Table view ###
#### accessory ####
<pre data-language="objc">
//UITableVieCellAccessoryDisclosureIndicator
//UITableVieCellAccessoryDisclosureButton
//UITableViewCellAccessoryCheckmark
//UITableViewCellAccessoryNone
accessoryType = UITableViewCellAccessoryDisclosureIndicator;
</pre>
<pre data-language="objc">
- (void) tableView:(UITableView * )tableView accessoryButtonTappedForRowWithIndexPath:(NSIndexPath * )indexPath {
}
</pre>
<pre data-language="objc">
UIButton * btn = [UIButton buttonWIthType:UIButtonTypeCustom];
btn addTarget:self action:@selector(function_name:) forControlEvents:UIControlEventTouchUpInside];
cell.accessoryView = btn;
</pre>
#### edit mode ####
<pre data-language="objc">
[self.tableView setEditing:!self.tableView.editing animated:YES];
</pre>
<pre data-language="objc">
UIBarButtonItem * b = [[UIBarButtonItem alloc] initWithTitle:@"" style:UIBarButtonItemStyleBordered target:self action:@selector(fun)];
self.navigationItem.rightBarButton Item = b
[b release];
</pre>
<pre data-language="objc">
- (UITableViewCell * )tableView:(UITableView * )tableView cellForRowAtIndexPath:(NSIndexPath * )indexPath {
	cell.showsRecorderControl = YES;
}

- (UITableViewCellEditingStyle)tableView:(UITableView * )tableView editingStyleForRowAtIndexPath:(NSIndexPath * )indexPath {
	return UITableViewCellEditingStyleNone;
}
- (BOOL)tableView:(UITableView * )tableView canMoveRowAtIndexPath:(NSIndexPath * )indexPath {
	return YES;
}
- (void)tableView:(UITableView * )tableView moveRowAtIndexPath:(NSIndexPath * )fromIndexPath toIndexPath:(NSIndexPath * )toIndexPath {
}
- (void)tableView:(UITableView * )tableView commitEditingStyle:(UITableViewCellEditingStyle) editingStyle forRowAtIndexPath:(NSIndexPath * )indexPath {
	[tableView deleteRowsAtInexPaths:[NSArray arrayWithObject:indexPath] withRowAnimation:UITableViewRowAnimationFade];
}
</pre>
<pre>
[self.tableView reloadData];
</pre>
## Chapter 10 Setting and Defaults##
### Setting ###
Resource - Settings Bundle: Settings.bundle - Root.plist
<pre>
Root Dictionary
	PreferenceSpecifiers Array
		Item 1 Dictionary
			Type PSGroupSpecifier
			Tile General Info
		Item 2 Dictionary
			Type String PSTextFieldSpecifier
			Title String Username
			Key String username
			AutocapitalizationType String None
			AutocorrectionType String No
		Item 3 Dictionary
			Type String PSTextFieldSpecifier
			Title String Password
			Key String password
			AutocapitalizationType String None
			AutocorrectionType String No
			IsSecure Boolean Yes 
		Item 4 Dictionary
			Type String PSMultiValueSpecifier
			Title String Protocol
			Key String protocol
			DefaultValue String SMTP
			Titles Array
				Item 1 String HTTP
				Item 2 String SMTP
				Item 3 String NNTP
				Item 4 String IMAP
				Item 5 String POP3
			Values Array
				Item 1 String HTTP
				Item 2 String SMTP
				Item 3 String NNTP
				Item 4 String IMAP
				Item 5 String POP3
		Item 5 Dictionary
			Type String PSToggleSwitchpecifier
			Title String WarpDriver
			Key String warp
			TrueValue String Engaged
			FalseValue String Disabled
			DefaultValue String Engaged
		Item 6 Dictionary
			Type PSGroupSpecifier
			Tile Warp Factor
		Item 7 Dictionary
				Type String PSSliderSpecifier
				Key String warpfactor
				DefaultValue String 5
				MinimumValue String 1
				MaximumValue String 10
				MinimumValueImage String min.png
				MaximumValueImage String max.png
		Item 8 Dictionary
			Type PSGroupSpecifier
			Tile Additional Info
		Item 9 Dictionary
			Type String PSSchildPaneSpecifier
			Tile String More Settings
			File String More
</pre>
### Defaults ###
<pre data-language="objc">
NSUserDefaults d = [NSUserDefaults standardUserDefaults];
[d setObject:@"value" forKey:@"key"];
[d objectForKey:@"key"];
</pre>

## Chapter 11 Data Persistence##
### File ###
<pre>
usr
	tmp
	Root
	Media
	Libary
		Preferences -- NSUserDefaults
	Applications
		Documents
		Library
		tmp
</pre>
#### Applications/Documents ####
<pre data-language="objc">
NSArray * paths = NSSearchPathForDirectoriesInDomains(NSDoumentDirectory, NSUserDomainMask, YES);
NSString * directory = paths[0]
NSString * file = [directory stringByAppendingPathComponent:@"filename"];
</pre>
#### Applications/tmp ####
<pre data-language="objc">
NSString * tmp = NSTemporaryDirectory();
NSString * f = [tmp stringByAppendingComponent:@"filename"];
</pre>
### Property List ###
Array Dictionary Data String Number Date
<pre data-language="objc">
//write
[obj writeToFile:@"path":atomically:YES];
//read
if ([NSFileManager defaultManager] fileExistsAtPath:filePath]) {
	obj = [[class alloc]initWithContentFile:filePath];
}
</pre>

### Archives ###
#### protocol ####
<pre data-language="objc">
#prama mark -
#prama mark NSCode
- (void) encodeWithCoder:(NSCoder * )encoder {
	[super encodeWithCoder:encode];
	[encode encodeObject: self.obj forKey: @"key"];
}

- (id) initWithCode: (NSCoder * )decoder {
	if (self = [super init]) {
		self.obj = [decoder decodeObjectForKey:@"key"];
	}
	return self;
}
#prama mark -
#prama mark NSCopying
- (id) copyWithZone:(NSZone * ) zone {
	Class * copy = [[self class] allocWithZone:zone] init];
	copy.obj = [[self.obj copyWithZone:zone] autorelease];
	return copy;
}
</pre>
#### write ####
<pre data-language="objc">
NSMutableData * data = [[NSMutableData alloc] init];
NSKeyedArchiver * archiver = [[NSKeyedArchiver alloc] initForWritingWithMutableData:data];
[archiver encodeObject:obj forKey:@"root"];
[archiver finishEncoding];
[data finishEncoding];
[data writeToFile: [self dataFilePath] atomically:YES];
[obj release];
[archiver release];
[data release];
</pre>
#### read ####
<pre data-language="objc">
NSData * data = [[NSMutableData alloc] initWithContentsOfFile: [self path]];
NSKeyedUnarchiver * unarchiver = [[NSKeyedUnarchiver alloc] initForReadingWithData: data];
Class * obj = [unarchiver decodeObjectForKey:@"root"];
[unarchiver finishDecoding];
//do something ...
[unarchiver release];
[data release];
</pre>
#### SQLite3 ####
<pre data-language="objc">
sqlite3 * db;
sqlite3_open([path UTF8String]);
char* err;
sqlite3_exec(db, sql, NUL, NULL, &err);
sqlite3_stmt * statement;
char * sql = "select id, value from tb";
sqlite3_prepare_v2(db, sql, -1, &statement, 0);
while (sqlite3_step(statement) == SQLITE_ROM) {
	int id = sqlite3_column_int(statement, 0);
	char* d = (char*)sqlite3_column_text(statement, 1);
	NSString value = [[NSString alloc] initWithUTF8String:d];
	//do something...
	[value release];
}

char * sql = "insert into tb values (?, ?);";
sqlite3_stmt * stmt;
if (sqlite3_prepare_v2(database, sql, -1, &stmt, nil) == SQLITE_OK) {
	sqlite3_bind_int(stmt, 1, 235);
	sqlite3_bind_text(stmt, 2, "value", -1, NULL);
}
if (sqlite3_step(stmt) != SQLITE_DONE) {
	//error to do something ...
}
sqlite3_finalize(stmt);
sqlite3_close(db);
</pre>
### Core Data ###
#### use core data storage ####
#### _Core_Data.xcdatamodel ####
#### Entity ####
#### Managed Object ####
#### Attribute ####
#### Relationship ####
#### Fetched property ####
#### persistent store (backing store) ####
* SQLite3, XML, memory store can be implemented for backing store
* backing store is created and configured in BIDAppDelegate 
#### Context ####
<pre data-language="objc">
NSManagedObjectContext ctx = [[[UIApplication sharedApplication] delegate] managedObjectContext];
</pre>
#### Create ####
<pre data-language="objc">
NSManagedObject * t = [NSEntityDescription insertNewObjectForEntityForName:@"s" inManagedObjectContext:ctx];
</pre>
#### Retrieve ####
<pre data-language="objc">
NSFetchRequest * r = [[NSFetchRequest alloc] init];
NSEntityDescription * ed= [NSEntityDescription entityForName:@"s" inManagedObjectContext:ctx];
[r setEntity:ed];
[ctx save:&e];
</pre>
<pre data-language="objc">
NSPredicate * pred = [NSPredicate predicateWithFormat:@"(s = %@)", s];
[r setPredicate: pred];
NSError * e;
NSArray * objs = [ctx executeFetchRequest:r error: &e];
if (objs == nil) {
	//error...
}
</pre>
### observer pattern ###
<pre data-language="objc">
[[NSNotificationCenter defaultCenter] addObserver:self selector:@selector(applicationWillTerminate:) name:UIApplicationWillTerminateNotification object:app];
</pre>

## Chapter 12 Quartz and OpenGL##
### Quartz 2D ###
The Quartz 2D API is part of the Core Graphics framework, so you may see Quartz referred to as Core Graphics or, simply, CG.
#### coordinate ####
#### CGPoint CGSize CGRect ####
<pre data-language="objc">
struct CGPoint {
	float x;
	float y;
};
struct CGSize {
	float width;
	float height;
};
struct CGRect {
	CGPoint origin;
	CGSize size;
};
</pre>
### UIColor ###
#### Mode:RGBA HSV HSL CMYK ####
#### Create and CGColor ####
<pre data-language="objc">
UIColor c = [UIColor colorWithRed:1.0f green:0.0f blue:0.0f alpha:1.0f];
c.CGColor;
</pre>
### Draw ###
<pre data-language="objc">
[self setNeedsDisplay];
- (void)drawRect:(CGRect)rect {
CGContextRef ctx = UIGraphicsGetCurrentContext();
CGContextSetLineWidth(ctx, 2.0);
CGContextSetStrokeColorWithColor(ctx, clr.CGColor);
//draw line
CGContextMoveToPoint(ctx, p1.x, p1.y);
CGContextAddLineToPoint(ctx, p2.x, p2.x);
CGContextStrokePath(ctx);

CGContextSetFillColorWithColor(ctx, clr.CGColor);
CGRect rc = CGRectMake(x, y, w, h);

//draw rect
CGContextAddRect(ctx, rc);
CGContextDrawPath(ctx, kCGPathFillStroke);
//draw ellipse
CGContextAddEllipseInRect(ctx, rc);
CGContextDrawPath(ctx, kCGPathFillStroke);
//draw image
[[UIImage imagedNamed:@"image.png"]drawAtPoint:p];
}
</pre>
### Optimizing ###
<pre data-language="objc">
CGRect dirty_rc = CRectUnion(old_rc, current_rc)
[self setNeedsDisplayInRect:dirty_rc];
</pre>
### OpenGL ES 
#### OpenGL ES = OpenGL Embeded System ####
#### OpenGL 3D coordinate to View 2D coordinate ####
#### Texture2D creates opengl 2d textures from images or text ####
#### draw ####
<pre data-language="objc">
//reset virtual world
glLoadIdentity();
//clean background
glClearColor(r, g, b, a);
glClear(GL_COLOR_BUFFER_BIT);
//set color
CGFloat c = CGColorGetComponents((CGColorRef)color.GCColor);
CGFloat * r = c[0];
CGFloat * g = c[1];
CGFloat * b = c[2];
glColor4f(r, g, b, 1.0);
//disable texture
gDisable(GL_TEXTURE_2D);
//convert to vertex point and draw vertex points
GLfloat vec[4];
vec[0] = p1.x;
vec[1] = self.frame.size.height - p1.y;
vec[2] = p2.x;
vec[3] = self.frame.size.height - p2.y;
gLineWidth(2.0);
glVertexPointer(2, GL_FLOAT, 0, vec);
glDrawArray(GL_LINES, 0, 2);
//render
glBindRenderbufferOES(GL_RENDERBUFFER_OES, viewRenderbuffer);
[context presentRenderbuffer:GL_RENDERBUFFER_OES];

//draw image
s = [[Texture2D alloc] initWithImage:[UIImage imaged:@"picture.png"]];
glBindTexture(GL_TEXTURE_2D, s.name);
glEnable(GL_TEXTURE_2D);
[s drawAtPoint:CGPointMake(x, self.fram.size.height - y)];
</pre>

## Chapter 13 Taps, Touches and Gestures##
### responder chain ###
### touches:the starting phase of the event ###
### event:representing the event. ###
<pre data-language="objc">
- (void) touchesBegan:(NSSet * )touches withEvent:(UIEvent * ) event {
	 
	[event touchesForView:self.view];
	UITouch t = [touches andObject];
	[t tapCount];
	CGPoint p = [t locationInView:self];
}
- (void) touchesCancelled:(NSSet * )touches withEvent:(UIEvent * ) event {
}
- (void) touchesEnded:(NSSet * )touches withEvent:(UIEvent * ) event {
}
- (void) touchesMoved:(NSSet * )touches withEvent:(UIEvent * ) event {
}
</pre>
## Chapter 14 Core Location##
three technologies:
* GPS
* cell ID location
* Wi-Fi
### start ###
<pre data-language="objc">
self.lmgr = [[CLLocationManger alloc] init];
locationManager.delegate = self;
//kCLLocationAccuracyNearestTenMeters
//kCLLocationAccuracyNearestHundredMeters
//kCLLocationAccuracyNearestKilometers
//kCLLocationAccuracyNearestThreeKilometers
locationManager.desiredAccuracy = kCLLocationAccuracyBest;
//float
locationManager.distanceFilter = kCLDistanceFilterNone;
[locationMnager startUpdatingLocation];
</pre>
### CLLocation ###
<pre data-language="objc">
CLLocationDegrees latitude = l.coordinate.latitude;
CLLocationDegrees longitude = l.coordinate.longitude;
CLLocationDistance altitude = l.altitude;
CLLocationAccuracy hAccuracy = l.horizontalAccuracy
CLLocationAccuracy vAccuracy = l.verticalAccuracy
CLLocationDistance distance = [from getDistanceFrom:to];
CLLocationDistance distance = [from getDistanceFrom:to];
</pre>
### delegate ###
<pre data-language="objc">
@interface where:UIViewController <CLLocationManagerDelegate> {
	CLLocationManager * lmgr;
}
@end

@implementation where
- (void) locationManager:(CLLocationManager * )manager didUpdateToLocation:(CLLocation * )newLocation fromLocation:(CLLocation * ) oldLocation {

}
- (void) locationManager:(CLLocationManager * )manager didFailWithError:(NSError * )error {
	error.code;
}
@end
</pre>

## Chapter 15 Accelerometer ##
### Hide status Bar ###
Info.plist UIStatusBarHidden Boolean
### Accelerometer ###
* portrait:y = -1.0
* upside down:y = 1.0
* landscape left:x = 1.0
* landscape right:x= -1.0
* laying with back:z = -1.0
* laying with front:z = 1.0
<pre data-language="objc">
UIAccelerometer * a = [UIAccelermeter sharedAccelerometer];
a.delegate = self;
a.updateInterval = 1.0f/6.0f;
</pre>
<pre data-language="objc">
@interface VCer:UIViewController <UIAccelerometerDelegate> {
}
</pre>
<pre data-language="objc">
- (void) accelerometer:(UIAccelerometer * ) accelerometer 
didAccelerate:(UIAcceleration * ) acceleration {
	//acceleration.x;
	//acceleration.y;
	//acceleration.z;
	
}
## Chapter 16 Camera and Photo Library##
<pre data-language="objc">
if ([UIIMagePickerController isSourceTypeAvailable: UIImagePickerControllerSourceTypePhotoLibrary]) {
	UIImagePickerController * picker = [[UIImagePickerController alloc] init];
	picker.delegate = self;
	//UIImagePickerControllerSourceTypeCamera
	//UIImagePickerControllerSourceTypeSavedPhotosAlbum
	picker.sourceType = UIImagePickerControllerSourceTypePhotoLibrary;
	[self presentModalViewController:picker animated:YES];
	[picker release];
}
</pre>
<pre data-language="objc">
@interface VCer:NSObject 
< UIIMagePickerControllerDelegate, UINavigationControllerDelegate > {
}
</pre>
<pre data-language="objc">
- (void)imagePickerController:(UIImagePickerController * )picker
didFinishPickingImage:(UIImage * )image
editingInfo:(NSDictionary * )editingInfo {
	UIImage * selectedImage = image;
	UIImage * originalImage = [editingInfo objectForKey: UIImagePickerControllerOriginalImage];
	//
	NSValue * cropRect = [editingInfo objectForKey:UIIMagePickerControllerCropRect];
	CGRect theRect = [cropRect CGRectValue];
	//TODO:
	[picker dismissModalViewControllerAnimated:YES];
}
- (void)imagePickerControllerDidCancel {
	[picker dismissModalViewControllerAnimated:YES];
}
</pre>

## Chapter 17 Localization ##
### Localiztion project (.lproj) ###
### The Localized String Macro(NSLocalizedString) ###
<pre data-language="objc">
NSLocale * locale = [NSLocale currentLocale];
NSString * displayNameString = [locale displayNameForKey:NSLocaleIdentifier value:[locale localeIdentifier]];
</pre>
### Localizing xib ###
### generating and localizing a string file ###
<pre data-language="shell">
genstring paths/all m files
</pre>




