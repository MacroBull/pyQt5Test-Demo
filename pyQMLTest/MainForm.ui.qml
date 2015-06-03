import QtQuick 2.4
import QtQuick.Controls 1.3
import QtQuick.Layouts 1.1

Item {
	id: item1
    width: 600
    height: 600

	property alias button1: button1
	property alias label1: label1
	property alias sliderHorizontal1: sliderHorizontal1

	ColumnLayout {
		id: columnLayout1
		anchors.rightMargin: 0
		anchors.bottomMargin: 0
		anchors.leftMargin: 0
		anchors.topMargin: 0
		anchors.fill: parent

		Label {
			id: label1
			height: 100
			text: qsTr("TextLabel")
			font.pointSize: 12
			anchors.right: parent.right
			anchors.left: parent.left
			anchors.top: parent.top
		}

		Rectangle {
			id: rect1
			height: 100
			anchors.bottom: button1.top
			anchors.bottomMargin: 0
			anchors.right: parent.right
			anchors.rightMargin: 0
			anchors.left: parent.left
			anchors.leftMargin: 0
			border.width: 1
			opacity: 0.4
		}

		Button {
			id: button1
			y: 318
			text: qsTr("PushButton")
			anchors.bottom: sliderHorizontal1.top
			anchors.bottomMargin: 0
			anchors.right: parent.right
			anchors.left: parent.left
		}

		Slider {
			id: sliderHorizontal1
			anchors.right: parent.right
			anchors.bottom: parent.bottom
			anchors.left: parent.left
			antialiasing: true
			transformOrigin: Item.Center
		}
	}
}
