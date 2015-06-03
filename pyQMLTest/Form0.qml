import QtQuick 2.4
import QtQuick.Controls 1.3

Item {
	width: 600
	height: 600

	property alias button1: form.button1

	MainForm {
		id: form
		anchors.fill: parent
		sliderHorizontal1.onValueChanged: {
			label1.text = sliderHorizontal1.value
			label1.rotation = sliderHorizontal1.value * -90
		}

		button1.onClicked: {
			label1.rotation = 0
			label1.text = 'Hello world!'
		}
	}

}
